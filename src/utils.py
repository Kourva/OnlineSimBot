#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library imports
from typing import ClassVar, NoReturn, Any


class User:
    """
    User class to get user details from From_User object
    """
    def __init__(self, user_obj: ClassVar[Any]) -> NoReturn:
        """
        Initial Method to initialize user data

        Parameters:
            user_obj (typing.ClassVar[Any]): User object

        Returns:
            None (typing.NoReturn)
        """
        # Get user's data
        self.id: int = user_obj.id                  # Chat ID
        self.un: str = user_obj.username            # Username
        self.fn: str = user_obj.first_name          # First name
        self.ln: str = user_obj.last_name           # Last name
        
    @property
    def pn(self) -> str:
        """
        Property method to return possible value for user's name

        Returns:
            name (str): possible name for user
        """
        # Return name
        return str(self.fn or self.ln or self.un or self.id)
        


def get_token() -> str:
    """
    Function to return Bot's token from token file

    Returns:
        token (str): Bot's Token
    """
    # Open and read token and return it
    with open("src/token.txt") as file:
        return file.read().strip()