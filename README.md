# Ultimate Pollbot ([@ultimate_pollbot](https://t.me/ultimate_pollbot))

[![MIT Licence](https://img.shields.io/badge/license-MIT-success.svg)](https://github.com/Nukesor/pollbot/blob/main/LICENSE.md)

![Alt Text](https://github.com/Nukesor/images/blob/main/pollbot.gif)

Deciding where you and your friends are going for lunch today can be a real hassle...
Or, for instance, deciding which games should be played at the next LAN-Party.

Since no other telegram poll/vote bot offered the full feature set my friends and I needed, I decided to write the ULTIMATE pollbot. A bot which combines all good features of all existing bots and even stuff beyond that.

## State of the project

The project is still actively maintained!
However, I **won't add any new features myself**, since I'm very happy with the current state of the bot.

Anyway, if you come up with a cool idea, I'll happily discuss it and review your pull requests.

Check the [official Trello board](https://trello.com/b/L3XfSRkN/ultimate-poll-bot) for the status of all requested features.
There's also a list of regularly requested "won't implement" features.

Upcoming bugs will of course be fixed as fast as possible.

## Features

The Ultimate Pollbot delivers a full set of well-tested and battle proven features.
It's capable of handling hundreds of voters for a single poll, while offering a high customizability and a wide range of different poll types to choose from.

Here is a list of the most important features:

### Poll types

This bot has 6 different vote modi. Each mode is useful for various scenarios. Choose wisely.

- Single vote: User get a single vote to allot
- Doodle: Users can vote with `yes`, `no` and `maybe` for each option.
- Block vote: Users can vote without restriction, but only one vote per option.
- Limited vote: Each user gets X votes for distribution, but only one vote per option.
- Cumulative vote: Every user gets X votes they can distribute as they like.
- Unlimited votes (Also called the shopping list): Every user can vote as often as they like, pretty much like a distributed shopping list.

### Anonymity settings

Polls can be configured to be anonymous, with the result that names of users are not visible.
Polls can be made anonymous subsequently, but as soon as a poll is anonymous it stays that way forever!

Further it's possible to hide the results of the poll until it gets closed.
As soon as such a poll is closed, the results will be visible. **Beware!**: such a poll cannot be reopened.

### Poll Management

- Addition and removal of options
- Allow other users to add new options
- Polls can be closed
- Polls can be reopened unless the poll is configured to hide the results until it has been closed.
- Polls can be completely deleted, which means that all non-forwarded occurrences of the poll will be removed.
- Polls can be reseted (Delete all votes). Poll needs to be closed first
- Polls can be cloned (New poll with same options, but without votes). Poll needs to be closed first

### Misc

- Internationalization
- Polls sync between groups in real time.
- Polls can be shared via link. This allows other users to spread the poll to arbitrary groups.
- A date picker for easier creation of poll options
- Specify a due date, at which the poll will be automatically closed.
- Activate notifications in chats to notify users that the poll will close soon.

### Sorting and Appearance

- Results can be displayed in a detailed or summarized manner.
- The percentage bar in the vote message can be disabled.
- The bot allows to configure the sorting of the option list and the user list for each option.
- Users can be sorted by vote date or username. Options can be sorted by highest percentage, name or by the order they've been added.

## Project Status

The project is still actively maintained. However, since my focus shifted to other projects, I most likely won't add new features myself.  
I'll still discuss and accept new feature requests and review feature PR's. Happy coding ;)

# Acknowledgements

<a href="https://sentry.io" ><img align="right" src="https://raw.githubusercontent.com/Nukesor/images/main/sentry.svg" alt="Packaging status"></a>
Thanks to Sentry for providing the project with a sponsored plan (which has super generous quotas!).

Thanks to [Lokalise](https://lokalise.co) for providing my projects with a free license for open-source development!

Thanks to the Turkish translator:

- [cnpltdncsln](https://github.com/cnpltdncsln)

Thanks to the Polish translator:

- [tszalbot](https://github.com/tszalbot)

Thanks to all Italian translators:

- [FedericoAntoniazzi](https://github.com/FedericoAntoniazzi)
- [LBindustries](https://github.com/LBindustries) for providing italian translations.  

Thanks to all Spanish translators:

- [balboag](https://github.com/balboag)
- [davidgfnet](https://github.com/davidgfnet)
- Miguel Antunez

Thanks to all Brazilian Portuguese translators:

- [gui258](https://github.com/gui258)
- Leonardo Frazao

Thanks to all German translators:

- Thorsten Schlaberg
- [KnorpelSenf](https://github.com/KnorpelSenf)

Thanks to the Catalan translator:

- [davidgfnet](https://github.com/davidgfnet)

Thanks to the Czech translator:

- Ignac (IgnacRR)

## Commands

```text
/start          Start the bot
/settings       Open the user settings menu
/create         Create a new poll
/list           List all active polls and manage them
/list_closed    List all closed polls and manage them
/notify         Activate notifications in a external chats
/help           Display the help
```

## Installation and Starting

Dependencies:

- [Poetry](https://python-poetry.org/) to manage and install dependencies.
- Ultimate Pollbot uses Postgres. Make sure the user has write/read rights. You can use [the provided docker-compose
 file](https://github.com/Nukesor/ultimate-poll-bot/blob/main/docker/docker-compose.yml) to set up a local development
  environment.

1. Clone the repository:

```bash
git clone git@github.com:nukesor/ultimate-poll-bot pollbot && cd pollbot
```

1. Execute `poetry install` to install all dependencies.
1. Either start the poll bot once with `poetry run python main.py` or copy the `pollbot.toml` manually to `~/.config
/pollbot.toml` and adjust all necessary values. On Windows, the tilde (`~`) will substitute to your home directory
, usually at `C:\Users\your.name\.config\pollbot.toml`.
1. Run `poetry run python initdb.py` to initialize the database (or recreate it, if necessary).
1. Start the bot by running `poetry run python main.py`.
1. If you plan to keep your database schema up-to-date, you need to set the current alembic revision manually with
 `poetry run alembic stamp head`.
1. Double-check if you are on the right revision `(head)` with `poetry run alembic current` and comparing it to `poetry run alembic history`.

### Devcontainer

When using the devcontainer e.g. with GitHub Codespaces you need to provide a Telegram bot name and its API key in the [config.py](pollbot/config.py) or set the variables `BOT_NAME` and `BOT_API_KEY` as GitHub Codespaces secrets .
You can start the bot with the `build dev (reset db)` task.

## Upgrading the Database

If you did Step 7 in the previous section, this is how you upgrade

1. Stop the bot
1. `git pull`
1. `poetry run alembic upgrade head` to run migrations on your database
1. Start the bot
