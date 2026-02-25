ABOUT_TEMPLATE = """# About Me

### 👋Hi, I'm {name}! ({role})

## Likes:

{likes}

## Motto:

> _{motto}_

## Contact:

{contact}
"""

def format_about(name: str, role: str, likes: tuple[str, ...], motto: str, contact: str) -> str:
    likes_formatted = "\n".join(f"- {like}" for like in likes)
    return ABOUT_TEMPLATE.format(
        name=name,
        role=role,
        likes=likes_formatted,
        motto=motto,
        contact=contact,
    )