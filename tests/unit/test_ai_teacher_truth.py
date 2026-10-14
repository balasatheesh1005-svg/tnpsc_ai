import re
import unittest

from core.ai_teacher import (
    ai_teacher,
    classify_evidence_confidence,
    extract_learner_safe_blocks,
    is_internal_metadata_key,
    normalize_query_terms,
    score_note_evidence,
    tokenize_text,
)


class TestAITeacherRetrievalTruth(unittest.TestCase):
    """
    P0 Batch 2: AI Teacher Retrieval Truth & Safety Test Suite.
    Validates token-boundary normalization, stop-word elimination,
    generic metadata extraction protection, deterministic ranking,
    honest semantic confidence, and zero internal ID leakage.
    """

    # --- Phase 2 & 3: Normalization & Token Boundary Tests ---

    def test_query_normalization_stop_word_removal(self):
        q = "when gst is implemented on"
        q_clean, all_tokens, meaningful = normalize_query_terms(q)
        self.assertEqual(all_tokens, ["when", "gst", "is", "implemented", "on"])
        self.assertEqual(meaningful, ["gst", "implemented"])
        self.assertNotIn("is", meaningful)
        self.assertNotIn("on", meaningful)
        self.assertNotIn("when", meaningful)

    def test_tamil_unicode_tokenization(self):
        q = "சிந்து சமவெளி நாகரிகம்"
        tokens = tokenize_text(q)
        self.assertEqual(tokens, ["சிந்து", "சமவெளி", "நாகரிகம்"])

    def test_substring_boundary_safety(self):
        # "is" and "on" must not match inside "administration"
        admin_tokens = set(tokenize_text("District Administration Framework"))
        self.assertNotIn("is", admin_tokens)
        self.assertNotIn("on", admin_tokens)
        self.assertIn("administration", admin_tokens)

    # --- Phase 4: Learner-Safe Extraction Policy ---

    def test_internal_metadata_keys_identified(self):
        self.assertTrue(is_internal_metadata_key("trap_id"))
        self.assertTrue(is_internal_metadata_key("table_id"))
        self.assertTrue(is_internal_metadata_key("node_id"))
        self.assertTrue(is_internal_metadata_key("id"))
        self.assertTrue(is_internal_metadata_key("meta"))
        self.assertTrue(is_internal_metadata_key("builder_metadata"))
        self.assertTrue(is_internal_metadata_key("category_id"))
        self.assertFalse(is_internal_metadata_key("title"))
        self.assertFalse(is_internal_metadata_key("points"))
        self.assertFalse(is_internal_metadata_key("definition"))

    def test_learner_safe_extraction_excludes_internal_ids(self):
        sample_node = {
            "content": {
                "tnpsc_traps": [
                    {
                        "trap_id": "trap_tamil_nilam_scope",
                        "title_en": "Tamil Nilam Portal Scope",
                        "points": {
                            "en": ["TRAP: Confusing Tamil Nilam with commercial portals.", "FACT: Official land records."]
                        },
                    }
                ],
                "comparison_tables": [
                    {
                        "id": "table_tn_digital_portals_services",
                        "title_en": "Digital Service Portals",
                        "rows_en": [["Tamil Nilam", "Revenue Dept", "Land records"]],
                    }
                ],
            }
        }
        blocks = extract_learner_safe_blocks(sample_node)
        full_text = " ".join(blocks)
        self.assertNotIn("trap_tamil_nilam_scope", full_text)
        self.assertNotIn("table_tn_digital_portals_services", full_text)
        self.assertIn("Tamil Nilam Portal Scope", full_text)
        self.assertIn("Official land records.", full_text)

    # --- Phase 7: Semantic Confidence Model ---

    def test_confidence_tiers_are_semantic_without_percentages(self):
        self.assertEqual(classify_evidence_confidence(60, ["phrase_match(gst)"]), "STRONG MATCH")
        self.assertEqual(classify_evidence_confidence(35, ["topic_token(gst)"]), "GOOD MATCH")
        self.assertEqual(classify_evidence_confidence(15, ["content_token(gst)"]), "LIMITED EVIDENCE")
        self.assertEqual(classify_evidence_confidence(5, []), "INSUFFICIENT EVIDENCE")

    # --- Phase 10: Canonical Retrieval Cases ---

    def test_case_1_when_gst_is_implemented_on(self):
        ans = ai_teacher("when gst is implemented on")
        self.assertIn("ECONOMY", ans.upper())
        self.assertIn("GST", ans.upper())
        self.assertNotIn("TN_ADMINISTRATION", ans.upper())
        self.assertNotIn("e-Governance", ans)
        self.assertNotIn("trap_tamil_nilam_scope", ans)
        self.assertNotIn("table_tn_digital_portals_services", ans)
        self.assertNotIn("100%", ans)
        self.assertIn("Evidence Confidence:", ans)
        self.assertIn("STRONG MATCH", ans)

    def test_case_2_gst_implemented_date(self):
        ans = ai_teacher("GST implemented date")
        self.assertIn("ECONOMY", ans.upper())
        self.assertIn("GST", ans.upper())
        self.assertIn("Evidence Confidence:", ans)

    def test_case_3_goods_and_services_tax(self):
        ans = ai_teacher("Goods and Services Tax")
        self.assertIn("ECONOMY", ans.upper())
        self.assertIn("GST", ans.upper())

    def test_case_4_article_279a(self):
        ans = ai_teacher("Article 279A")
        # Article 279A should retrieve either GST or Finance Commission comparison table
        self.assertIn("ECONOMY", ans.upper())
        self.assertTrue("GST" in ans.upper() or "FINANCE COMMISSION" in ans.upper())
        self.assertIn("Evidence Confidence:", ans)

    def test_case_5_stop_words_only_abstains(self):
        ans = ai_teacher("is on the")
        self.assertIn("Answer கிடைக்கவில்லை", ans)
        self.assertIn("reliable evidence", ans)
        self.assertNotIn("Evidence Confidence:", ans)

    def test_case_6_nonsense_query_abstains(self):
        ans = ai_teacher("asdfghjkl zxcvbnm 99999")
        self.assertIn("Answer கிடைக்கவில்லை", ans)
        self.assertIn("reliable evidence", ans)

    def test_case_7_history_indus_valley(self):
        ans = ai_teacher("Indus Valley Civilization")
        self.assertIn("HISTORY", ans.upper())
        self.assertIn("INDUS VALLEY", ans.upper())
        self.assertIn("STRONG MATCH", ans)

    def test_case_8_polity_preamble(self):
        ans = ai_teacher("Preamble of the Constitution")
        self.assertIn("POLITY", ans.upper())
        self.assertIn("PREAMBLE", ans.upper())

    def test_case_9_internal_metadata_leakage_prevented(self):
        queries = ["e-Governance Tamil Nadu", "Tamil Nilam", "when gst is implemented on", "digital portals"]
        for q in queries:
            ans = ai_teacher(q)
            self.assertNotIn("trap_tamil_nilam_scope", ans)
            self.assertNotIn("table_tn_digital_portals_services", ans)
            self.assertNotIn(".json", ans)
            self.assertNotIn("data/notes", ans)

    def test_case_10_tamil_query_indus_valley(self):
        ans = ai_teacher("சிந்து சமவெளி நாகரிகம்")
        self.assertIn("HISTORY", ans.upper())
        self.assertTrue("INDUS VALLEY" in ans.upper() or "சிந்து" in ans)

    # --- Phase 11: Adversarial Retrieval Tests ---

    def test_adversarial_stopword_collisions(self):
        # Solitary stop words must abstain
        for word in ["is", "on", "in", "the", "when", "what"]:
            ans = ai_teacher(word)
            self.assertIn("Answer கிடைக்கவில்லை", ans)

    def test_adversarial_meaningful_token_dominance_over_stopwords(self):
        ans = ai_teacher("what did the ivc people do when")
        self.assertIn("HISTORY", ans.upper())
        self.assertIn("INDUS VALLEY", ans.upper())

    def test_adversarial_administration_boundary(self):
        ans = ai_teacher("District Administration in Tamil Nadu")
        self.assertIn("TN_ADMINISTRATION", ans.upper())


if __name__ == "__main__":
    unittest.main()
