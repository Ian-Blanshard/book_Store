from playwright.sync_api import Page, expect

def test_user_can_login(page: Page, db_connection):
    db_connection.seed('seeds/user_seeds.sql')
    db_connection.execute("INSERT INTO users (username, password) values ('test_user1','1234');")
    page.goto('http://127.0.0.1:5001/sessions/new')
    page.get_by_label("username").fill("test_user1")
    page.get_by_label("password").fill("1234")
    page.get_by_role("button").click()
    h1 = page.locator("h1")
    expect(h1).to_have_text("Welcome to AceReads")

def test_user_failed_login(page: Page, db_connection):
    db_connection.seed('seeds/user_seeds.sql')
    db_connection.execute("INSERT INTO users (username, password) values ('test_user1','1234');")
    page.goto('http://127.0.0.1:5001/sessions/new')
    page.get_by_label("username").fill("test_user1")
    page.get_by_label("password").fill("wrongpassword")
    page.get_by_role("button").click()
    h1 = page.locator("h1")
    expect(h1).to_have_text("Login")

