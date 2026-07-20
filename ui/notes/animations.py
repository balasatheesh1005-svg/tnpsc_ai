import streamlit as st


def inject_animations_css():
    """Injects keyframe CSS animations for micro-interactions and transitions."""
    st.markdown(
        """
        <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes pulseGlow {
            0% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(37, 99, 235, 0); }
            100% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0); }
        }

        @keyframes shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }

        .animate-fade-in {
            animation: fadeIn 0.4s ease-out forwards;
        }

        .animate-pulse-glow {
            animation: pulseGlow 2s infinite;
        }

        .shimmer-badge {
            background: linear-gradient(90deg, #3B82F6 0%, #60A5FA 50%, #3B82F6 100%);
            background-size: 200% 100%;
            animation: shimmer 3s infinite;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
