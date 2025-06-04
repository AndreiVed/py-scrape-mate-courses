from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup, Tag

BASE_URL = "https://mate.academy/"


@dataclass
class Course:
    name: str
    short_description: str
    duration: str


def parse_single_course(course: Tag) -> Course:
    return Course(
        name=course.select_one(".ProfessionCard_title__m7uno").text,
        short_description=course.select_one(
            ".ProfessionCard_description__K8weo").text,
        duration=course.select_one(".ProfessionCard_duration__13PwX").text
    )


def get_all_courses() -> list[Course]:
    text = requests.get(BASE_URL).content
    soup = BeautifulSoup(text, "html.parser")
    courses = soup.select(".ProfessionCard_cardWrapper__BCg0O")
    return [parse_single_course(course) for course in courses]


def main() -> None:
    get_all_courses()


if __name__ == "__main__":
    main()
