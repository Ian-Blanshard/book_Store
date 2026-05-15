from playwright.sync_api import Page, expect

def test_has_h1(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    h3 = page.locator("h3")
    expect(h3).to_have_text("Films Acereads has available")

def test_film_list_contains_all_films(page: Page, db_connection):
    db_connection.seed("seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    films = page.locator('.list-group-item')
    expected_films = [
        'Dune Part I released 2021',
        'Dune Part II released 2024',
        'Serenity released 2005'
    ]    
    actual_films = films.all_inner_texts()
    assert actual_films == expected_films


def test_creating_film_with_form(page: Page, db_connection):
    db_connection.seed("seeds/films.sql")
    db_connection.execute("TRUNCATE TABLE users;")
    db_connection.execute("INSERT INTO users (username, password) values ('testuser', 'testpassword');")
    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_label("username").fill("testuser")
    page.get_by_label("password").fill("testpassword")
    page.get_by_role("button").click()
    page.goto("http://127.0.0.1:5001/new_film")
    page.get_by_label("Film title").fill("A Complete Unknown")
    page.get_by_label("Release year").fill("2024")
    page.get_by_role("button", name="Submit").click()
    films = page.locator('.list-group-item')
    expected_films = [
        'Dune Part I released 2021',
        'Dune Part II released 2024',
        'Serenity released 2005',
        'A Complete Unknown released 2024'
    ]   
    assert films.all_inner_texts() == expected_films 

def test_unauthorised_user_attempt_add_film(page: Page):
    page.goto("http://127.0.0.1:5001/new_film")
    h3 = page.locator('h3')
    expect(h3).to_have_text('Login')
