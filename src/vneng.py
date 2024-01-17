#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library imports
from typing import ClassVar, NoReturn, List, Dict, Any

# Related third party module imports
import requests


class VNEngine:
    """
    Virtual Number Engine
    """
    def __init__(self) -> NoReturn:
        """
        Initial method to initialize variables for engine

        Returns:
            None (typing.NoReturn)
        """
        # Set the initial URLs and Endpoints
        self.lang: str = "?lang=en"
        self.base: str = "https://onlinesim.io/"
        self.endpoint: str = "api/v1/free_numbers_content/"
        self.country_url: str = f"{self.base}{self.endpoint}countries"

    def get_online_countries(self) -> List[Dict[str, str]]:
        """
        Method to get details about available countries

        Returns:
            countries (list): Online countries
        """
        # Send request to API endpoint
        response: ClassVar[Any] = requests.get(url=self.country_url).json()

        # Process countries and filter them based on status
        if response["response"] == "1":
            all_countries: List[Dict[str, str]] = response["counties"]

        # Filter numbers based on their online status
        online_countries: List[Dict[str, str]] = list(
            filter(lambda x:x["online"] == True , all_countries)
        )

        # Return data
        return online_countries

    def get_country_numbers(self, country: str) -> List[Dict[str, str]]:
        """
        Method to get specific country numbers like Russia

        Parameters:
            country (str): country name for e.g. Russia, Spain

        Returns:
            numbers (list): List of available number for that country
        """

        # Set URL endpoint
        numbers_url: str = f"{self.country_url}/{country}{self.lang}"

        # Send request and get numbers
        response: ClassVar[Any] = requests.get(url=numbers_url).json()

        # Process numbers and extract number codes from data
        if response["response"] == "1":
            numbers: List[Dict[str, str]] = list(
                map(lambda x:(x["data_humans"], x["full_number"]), response["numbers"])
            )
            # return data
            return numbers
        else:
            return False

    def get_number_inbox(self, country: str, number: str) -> Dict[str, str]:
        """
        Method to get inbox messages of specific number

        Parameters:
            country (str): country name for e.g. Russia, Spain
            number (str): number code for the country

        Returns:
            detail (list): List of messages in number's inbox 
        """

        # Set URL endpoint
        number_detail_url: str = f"{self.country_url}/{country}/{number}{self.lang}"

        # Request the endpoint and get data
        response: ClassVar[Any] = requests.get(url=number_detail_url).json()

        # Process data and extract details
        if response["response"] == "1" and response["online"]:
            # Get inbox messages
            messages: List[Dict[str, str]] = list(
                map(lambda x:{x["data_humans"]: x["text"]} , response["messages"]["data"])
            )
            # Return data
            return messages

        else:
            return False
