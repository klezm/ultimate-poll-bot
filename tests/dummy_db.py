from pollbot.display.poll.option import get_percentage_style_bar
from pollbot.models import User, Poll, Option, Vote
from pollbot.enums import PollType

# usr1 = User(
#     user_id = 1,
#     username = "user1",
# )
# usr1.name = "User 1"

# # poll1 = Poll.create(usr1, session)
# poll1 = Poll(usr1)
# poll1.name = "Title (poll 1)"
# poll1.description = "Description (poll 1)"

# poll1.options = [Option(poll1, "option 1"), Option(poll1, "option 2")]
# unicode_blocks = [get_percentage_style_bar(width = 1, filled_slots = 0, percentage = x / 7) for x in range(7)]
# poll1.options += [Option(poll1, x) for x in unicode_blocks]

# poll1.poll_type = PollType.count_vote.name
# poll1.percentage_style = "bar"  # box bar


def dummy_db(poll, session, user):

    usr1 = User(
        user_id = 1,
        username = "user1",
    )
    usr1.name = "User 1"
    usrs = [User(user_id = x, username = f"user{x}") for x in range(2, 5)]
    # for us in usrs: us.name = f"User {us.user_id}"

    poll.name += " (you found the dev mode!)"
    poll.description = "Description (poll 1)"

    # poll.options = [Option(poll, "option 0"), Option(poll, "option 1")]
    unicode_blocks = [get_percentage_style_bar(width = 1, filled_slots = 0, percentage = x / 7)[1:-1    ] for x in range(7)]
    unicode_blocks += [unicode_blocks[-1] + x for x in unicode_blocks]
    # poll.options += [Option(poll, x) for x in unicode_blocks]
    for x in unicode_blocks:
        Option(poll, x)

    poll.poll_type = PollType.count_vote.name
    poll.percentage_style = "bar"  # box bar

    for iu, user in enumerate([user, usr1] + usrs):
        for i, option in enumerate(poll.options):
            session.add(option)
            vote = Vote(user, option)
            vote.vote_count = int(2 ** (.6 * i) / (iu + 1))
            vote.priority = 0
            session.add(vote)
        session.commit()
