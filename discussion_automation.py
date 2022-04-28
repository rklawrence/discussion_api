import requests
from random import choice
from datetime import datetime, timedelta
from time import sleep
from random import randrange

ACCESS_TOKEN = ""

messages = [""]

def generate_message() -> str:
    emotion_list = ["Ecstatic",
                    "Overjoyed",
                    "Blissful",
                    "Exhilarated",
                    "Animated",
                    "Amazed",
                    "Astonished",
                    "Delighted",
                    "Pleased",
                    "Cheerful",
                    "Jolly",
                    "Jovial",
                    "Jubilation",
                    "Gleeful",
                    "Vibrant",
                    "Triumphant",
                    "Victorious",
                    "Glorious",
                    "Exultant",
                    "Exuberance",
                    "Spirited",
                    "Energetic",
                    "Festive",
                    "Light-hearted",
                    "Mirthful",
                    "Upbeat",
                    "Splendid",
                    "Jaunty",
                    ]

    random_thoughts = [ "The scream in your head will never be out of breath.",
                        "Do fish in water have their hidden life where they go to school, hang out, study, and get married?",
                        "If everyone had roller skates instead of feet, would there be cars or would they go rollerblading everywhere?",
                        "We will never know what memories we had as children and we will never remember them.",
                        "We know our parents for whole our life, while they know us only part of their lives.",
                        "Someone was born at this very moment, and someone lost his life at this very moment.",
                        "Our brain has never experienced some things, and yet it can tailor a scenario in its head as if it had happened.",
                        "If the tomato is a fruit, then ketchup is the jam.",
                        "If I were a book, what title would I have?",
                        "Valentine’s Day is known for its red color, red roses, red hearts … Would it be strange if another color was used for Valentine’s Day instead of red? And why red? Why does red associate us with love?",
                        "The hospital where you were born is the only building you left without entering.",
                        "Humans invented the sounds produced by dinosaurs.",
                        "Maybe it’s better not to kill the spider, because if I kill him, his family and friends can come to the funeral and in that way, I will summon many more spiders.",
                        "Who invented the words and names of certain objects and how did it occur to someone to call a chair just like that – “chair”?",
                        "How does our voice in our head sound?",
                        ]
    fun_activities = [
        "doing archery",
        "cooking",
        "playing ping-pong",
        "making stained glass",
        "watching youtube videos",
        "Playing D&D"
    ]
    styles = ["thought", "activity", "activity"]
    style = choice(styles)
    if style == "emotion":
        emotion = choice(emotion_list).lower()
        message = f"5: I am feeling {emotion}."
    elif style == "thought":
        thought = choice(random_thoughts)
        message = f"7. Reading shower thoughts, the one I enjoyed most recently was \"{thought}\""
    elif "activity":
        activity = choice(fun_activities)
        message = f"7. I enjoy {activity}."
    return message


def post_discussion_entry(course_id: int, discussion_id: int) -> int:
    url = f"https://canvas.unl.edu/api/v1/courses/{course_id}/discussion_topics/{discussion_id}/entries"
    message = generate_message()
    print(message)
    request = requests.post(url, data={"message": message}, params={"access_token":ACCESS_TOKEN}, allow_redirects=False)
    return request.text


def get_discussion_entries(course_id: int, discussion_id: int) -> str:
    url = f"http://canvas.unl.edu/api/v1/courses/{course_id}/discussion_topics/{discussion_id}/entries"
    request = requests.get(url, params={"access_token": ACCESS_TOKEN})
    return request.text


# def get_non_commented_dates(course_id: int, discussion_id: int, user_id: int) -> list:
#     url = f"http://canvas.unl.edu/api/v1/courses/{course_id}/discussion_topics/{discussion_id}/entries?user_id={user_id}"
#     params = {"access_token": ACCESS_TOKEN}
#     request = requests.get(url, params=params)
#     # print(request.json())
#     print(request.text)
#     json_data = request.json()
#     # print(len(json_data))
#     for response in json_data:
#         print(response)
#     pass

def makeup_checkin(course_id: int, discussion_id: int) -> None:
    url = f"https://canvas.unl.edu/api/v1/courses/{course_id}/discussion_topics/{discussion_id}/entries"

    dates = [
        datetime(2022, 2, 22),
        datetime(2022, 3, 1),
        datetime(2022, 3, 10),
        datetime(2022, 3, 24),
        datetime(2022, 3, 29),
        datetime(2022, 3, 31),
        datetime(2022, 4, 12),
        datetime(2022, 4, 22),
        datetime(2022, 4, 26),
    ]
    current_date = datetime(2022, 2, 22)
    end_date = datetime(2022, 4, 25)
    generated_messages = list()
    while current_date < end_date:
        if current_date not in dates:
            date_string = current_date.strftime("%b. %-d")
            message = f"This is making up for {date_string}: "
            candidate_message = ""
            while candidate_message in messages:
                candidate_message = generate_message()
            messages.append(candidate_message)
            message += candidate_message
            print(message)
            generated_messages.append(message)
        if current_date.weekday() == 1:
            add_date = 2
        else:
            add_date = 5
        current_date += timedelta(days=add_date)
        if current_date in dates:
            print("duplicate date")

    for message in generated_messages:
        request = requests.post(url, data={"message": message}, params={"access_token":ACCESS_TOKEN}, allow_redirects=False)
        if request.status_code != 200:
            print(f"There was an error posting {message}")
            print(f"Response: {request.text}")
            break
        sleep(randrange(180, 300))



if __name__ == '__main__':
    course_id = 123218
    discussion_id = 895856
    user_id = 118864
    # makeup_checkin(course_id, discussion_id)
    # print(len(messages))
    # response = post_discussion_entry(course_id=course_id, discussion_id=discussion_id)
    # print(response)
    # get_non_commented_dates(course_id=course_id, discussion_id=discussion_id, user_id=user_id)