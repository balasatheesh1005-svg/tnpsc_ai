def get_bookmarks(state, key):
    return list(state.get(key, []))


def is_bookmarked(state, key, question_id):
    return str(question_id) in set(get_bookmarks(state, key))


def toggle_bookmark(state, key, question_id):
    question_id = str(question_id or "").strip()
    if not question_id:
        return get_bookmarks(state, key)

    bookmarks = get_bookmarks(state, key)
    if question_id in bookmarks:
        bookmarks.remove(question_id)
    else:
        bookmarks.append(question_id)

    state[key] = bookmarks
    return bookmarks

