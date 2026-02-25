#!/usr/bin/env python3

from dataclasses import dataclass

from about_template import format_about

@dataclass
class About:
    name: str = "snow7y"
    role: str = "Software Engineer"
    likes: tuple[str, ...] = ("Python 🐍", "AI Coding 🤖", "Coffee ☕")
    motto: str = "Products that benefit people"
    contact: str = "contact@snow7y.net"

if __name__ == "__main__":
    me = About()
    output = format_about(
        name=me.name,
        role=me.role,
        likes=me.likes,
        motto=me.motto,
        contact=me.contact,
    )
    print(output)
