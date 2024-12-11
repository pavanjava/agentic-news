from asknews_sdk import AskNewsSDK
from dotenv import load_dotenv, find_dotenv
from asknews_utils.news_encoder import create_json_response
from typing import Any
import os

load_dotenv(find_dotenv())


def asknews_news_client():
    ask = AskNewsSDK(
        client_id=os.environ.get("ASK_NEWS_CLIENT_ID"),
        client_secret=os.environ.get("ASK_NEWS_SECRET"),
        scopes={"news"}
    )
    return ask


def query_political_news(query_str: str, continents: str, country_code: str) -> Any:
    """Use this function to get top news related to technology.

    Args:
        query_str (str): the user query to search for technology news.
        continents (str): specific news from the geographic region (continent)
        country_code (str): specific news in a specific country within the continents.
    Returns:
        str: JSON object of top story summaries.
    """
    print(f"Calling political Tool with, query_str: {query_str}, continents: {continents}")
    response = asknews_news_client().news.search_news(
        query=query_str,  # your keyword query
        n_articles=10,  # control the number of articles to include in the context
        return_type="dicts",  # you can also ask for "dicts" if you want more information
        method="both",  # use "nl" for natural language for your search, or "kw" for keyword search
        continents=[continents],
        countries=[country_code],
        categories=["Politics"],
        strategy='latest news'
    )

    return create_json_response(response)


def query_business_news(query_str: str, continents: str, country_code: str) -> Any:
    """Use this function to get top news related to business

    Args:
        query_str (str): the user query to search for business news.
        continents (str): specific news from the geographic region (continent).
        country_code (str): specific news in a specific country within the continents.
    Returns:
        str: JSON object of top story summaries.
    """
    print(f"Calling business tool with, query_str: {query_str}, continents: {continents}")
    response = asknews_news_client().news.search_news(
        query=query_str,  # your keyword query
        n_articles=10,  # control the number of articles to include in the context
        return_type="dicts",  # you can also ask for "dicts" if you want more information
        method="both",  # use "nl" for natural language for your search, or "kw" for keyword search,
        continents=[continents],
        countries=[country_code],
        categories=["Business"],
        strategy='latest news'
    )

    return create_json_response(response)


def query_crime_news(query_str: str, continents: str, country_code: str) -> Any:
    """Use this function to get top news related to Crime

    Args:
        query_str (str): the user query to search for business news.
        continents (str): specific news from the geographic region (continent).
        country_code (str): specific news in a specific country within the continents.
    Returns:
        str: JSON object of top story summaries.
    """
    print(f"Calling crime tool with, query_str: {query_str}, continents: {continents}")
    response = asknews_news_client().news.search_news(
        query=query_str,  # your keyword query
        n_articles=10,  # control the number of articles to include in the context
        return_type="dicts",  # you can also ask for "dicts" if you want more information
        method="both",  # use "nl" for natural language for your search, or "kw" for keyword search,
        continents=[continents],
        countries=[country_code],
        categories=["Crime"],
        strategy='latest news'
    )

    return create_json_response(response)


def query_sports_news(query_str: str, continents: str, country_code: str) -> Any:
    """Use this function to get top news related to Sports

    Args:
        query_str (str): the user query to search for business news.
        continents (str): specific news from the geographic region (continent).
        country_code (str): specific news in a specific country within the continents.
    Returns:
        str: JSON object of top story summaries.
    """
    print(f"Calling sports tool with, query_str: {query_str}, continents: {continents}")
    response = asknews_news_client().news.search_news(
        query=query_str,  # your keyword query
        n_articles=10,  # control the number of articles to include in the context
        return_type="dicts",  # you can also ask for "dicts" if you want more information
        method="both",  # use "nl" for natural language for your search, or "kw" for keyword search,
        continents=[continents],
        countries=[country_code],
        categories=["Sports"],
        strategy='latest news'
    )

    return create_json_response(response)


def query_science_and_tech_news(query_str: str, continents: str, country_code: str) -> Any:
    """Use this function to get top news related to Science & Technology

    Args:
        query_str (str): the user query to search for business news.
        continents (str): specific news from the geographic region (continent).
        country_code (str): specific news in a specific country within the continents.
    Returns:
        str: JSON object of top story summaries.
    """
    print(f"Calling science & technology tool with, query_str: {query_str}, continents: {continents}")
    response = asknews_news_client().news.search_news(
        query=query_str,  # your keyword query
        n_articles=10,  # control the number of articles to include in the context
        return_type="dicts",  # you can also ask for "dicts" if you want more information
        method="both",  # use "nl" for natural language for your search, or "kw" for keyword search,
        continents=[continents],
        countries=[country_code],
        categories=["Science", "Technology"],
        strategy='latest news'
    )

    return create_json_response(response)


def query_finance_news(query_str: str, continents: str, country_code: str) -> Any:
    """Use this function to get top news related to Finance

    Args:
        query_str (str): the user query to search for business news.
        continents (str): specific news from the geographic region (continent).
        country_code (str): specific news in a specific country within the continents.
    Returns:
        str: JSON object of top story summaries.
    """
    print(f"Calling finance tool with, query_str: {query_str}, continents: {continents}")
    response = asknews_news_client().news.search_news(
        query=query_str,  # your keyword query
        n_articles=10,  # control the number of articles to include in the context
        return_type="dicts",  # you can also ask for "dicts" if you want more information
        method="both",  # use "nl" for natural language for your search, or "kw" for keyword search,
        continents=[continents],
        countries=[country_code],
        categories=["Finance"],
        strategy='latest news'
    )

    return create_json_response(response)


def query_military_news(query_str: str, continents: str, country_code: str) -> Any:
    """Use this function to get top news related to Military

    Args:
        query_str (str): the user query to search for military news.
        continents (str): specific news from the geographic region (continent).
        country_code (str): specific news in a specific country within the continents.
    Returns:
        str: JSON object of top story summaries.
    """
    print(f"Calling military tool with, query_str: {query_str}, continents: {continents}")
    response = asknews_news_client().news.search_news(
        query=query_str,  # your keyword query
        n_articles=10,  # control the number of articles to include in the context
        return_type="dicts",  # you can also ask for "dicts" if you want more information
        method="both",  # use "nl" for natural language for your search, or "kw" for keyword search,
        continents=[continents],
        countries=[country_code],
        categories=["Military"],
        strategy='latest news'
    )

    return create_json_response(response)


def query_health_news(query_str: str, continents: str, country_code: str) -> Any:
    """Use this function to get top news related to Health

    Args:
        query_str (str): the user query to search for health news.
        continents (str): specific news from the geographic region (continent).
        country_code (str): specific news in a specific country within the continents.
    Returns:
        str: JSON object of top story summaries.
    """
    print(f"Calling health tool with, query_str: {query_str}, continents: {continents}")
    response = asknews_news_client().news.search_news(
        query=query_str,  # your keyword query
        n_articles=10,  # control the number of articles to include in the context
        return_type="dicts",  # you can also ask for "dicts" if you want more information
        method="both",  # use "nl" for natural language for your search, or "kw" for keyword search,
        continents=[continents],
        countries=[country_code],
        categories=["Health"],
        strategy='latest news'
    )

    return create_json_response(response)


def query_climate_news(query_str: str, continents: str, country_code: str) -> Any:
    """Use this function to get top news related to Climate

    Args:
        query_str (str): the user query to search for climate news.
        continents (str): specific news from the geographic region (continent).
        country_code (str): specific news in a specific country within the continents.
    Returns:
        str: JSON object of top story summaries.
    """
    print(f"Calling climate tool with, query_str: {query_str}, continents: {continents}")
    response = asknews_news_client().news.search_news(
        query=query_str,  # your keyword query
        n_articles=10,  # control the number of articles to include in the context
        return_type="dicts",  # you can also ask for "dicts" if you want more information
        method="both",  # use "nl" for natural language for your search, or "kw" for keyword search,
        continents=[continents],
        countries=[country_code],
        categories=["Climate"],
        strategy='latest news'
    )

    return create_json_response(response)
