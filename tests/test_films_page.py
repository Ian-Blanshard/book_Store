from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_has_h1(page: Page):
    page.goto("http://127.0.0.1:5001/films")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Films Acereads has available")

def test_film_list_contains_all_films(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")

    books = page.locator('.list-group-item')

    expected_books = [
        'Dune Part I released 2021',
        'Dune Part II released 2024',
        'Serenity released 2005'
    ]    

    # here's the neat part which saves you from iterating over the `li` elements
    actual_books = books.all_inner_texts()

    assert actual_books == expected_books
