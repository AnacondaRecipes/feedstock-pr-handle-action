#!/usr/bin/env python3

import json
import os


def get_event():
    """
    Reading the raw Gtihub event from json
    :return: The raw GitHub event loaded from json
    """
    with open(os.environ.get("GITHUB_EVENT_PATH"), "r") as fd:
        event = json.loads(fd.read())
    return event


def main():
    event = get_event()
    print(json.dumps(event, sort_keys=True, indent=4))


if __name__ == "__main__":
    print("==================================================================")
    print("START: Running Pull Request Action!")
    main()
    print("==================================================================")
    print("END: Finished")
