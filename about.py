#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class About:
    name: str = "snow7y"
    role: str = "Software Engineer"
    likes: list[str] = ("Python", "AI Coding", "Coffee")
    motto: str = "Products that benefit people"

if __name__ == "__main__":
    me = About()
    print(f"Hi, I'm {me.name} ({me.role})")
    print(f"I like {', '.join(me.likes)}")
    print(f"motto = {me.motto}")
