from playwright.sync_api import Page, expect

def test_books_title_correct(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    h1 = page.locator('h1')
    expect(h1).to_have_text('Books Acereads has available')


def test_list_elements_have_correct_text(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    li_items = page.locator('li')
    assert li_items.all_inner_texts() == ['The Gruffalo', 'Julia Donaldson',
                                    'Ada Twist, Scientist', 'Andrea Beaty',
                                    'The Girl Who Drank the Moon', 'Kelly Barnhill',
                                    'Dragons in a Bag', 'Zetta Elliott']