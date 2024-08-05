import argparse


class Argument_Parser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="CLI for managing test environments")
        self._add_arguments()
        self.parse_arguments = self.parser.parse_args()

    def _add_arguments(self):
        self.parser.add_argument("--remote", action="store",
                                 default="false",
                                 choices=["true", "false"], help="Run tests on LambdaTest (true/false)")

    def get_remote(self):
        self.remote = self.parse_arguments.remote
        return self.remote == "true"
