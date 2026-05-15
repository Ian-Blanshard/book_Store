from playwright.sync_api import Page, expect

def test_books_title_correct(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    h3 = page.locator('h3')
    expect(h3).to_have_text('Books Acereads has available')

def test_list_elements_have_correct_text(page: Page, db_connection):
    db_connection.seed('seeds/books_seed.sql')
    page.goto("http://127.0.0.1:5001/books")
    li_items = page.locator('.list-group-item')
    assert li_items.all_inner_texts() == ['The Gruffalo by Julia Donaldson',
                                    'Ada Twist, Scientist by Andrea Beaty',
                                    'The Girl Who Drank the Moon by Kelly Barnhill',
                                    'Dragons in a Bag by Zetta Elliott']
    
def test_add_book_form(page: Page, db_connection):
    db_connection.seed('seeds/books_seed.sql')
    db_connection.execute("TRUNCATE TABLE users;")
    db_connection.execute("INSERT INTO users (username, password) values ('testuser', 'testpassword');")
    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_label("username").fill("testuser")
    page.get_by_label("password").fill("testpassword")
    page.get_by_role("button").click()
    page.goto("http://127.0.0.1:5001/new_book")
    page.get_by_label("title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_label("author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    li_items = page.locator('.list-group-item')
    assert li_items.all_inner_texts() == ['The Gruffalo by Julia Donaldson',
                                    'Ada Twist, Scientist by Andrea Beaty',
                                    'The Girl Who Drank the Moon by Kelly Barnhill',
                                    'Dragons in a Bag by Zetta Elliott',
                                    'The Chroicles of Geronimo (the cat) by Geronimo'
                                    ]
    
def test_unauthorised_user_attempt_add_book(page: Page):
    page.goto("http://127.0.0.1:5001/new_book")
    h3 = page.locator('h3')
    expect(h3).to_have_text('Login')
    