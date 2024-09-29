from playwright.sync_api import Page, expect

# Run server before start: 'python -m http.server 8000' and site at '127.0.0.1:8000'

BASE_URL = 'http://127.0.0.1:8000'


def test_cube_of_a_number(page:Page):
    page.goto(BASE_URL)

    input= page.get_by_placeholder('enter number...')
    input.fill('10')

    cube_btn = page.get_by_role('button', name='Cube')
    cube_btn.click()

    result_field = page.locator('css=p#result')
    expect(result_field).to_contain_text('1000')



def test_cube_of_empty_input(page:Page):
    page.goto(BASE_URL)

    input= page.get_by_placeholder('enter number...')
    input.fill('')

    cube_btn = page.get_by_role('button', name='Cube')
    cube_btn.click()

    result_field = page.locator('css=p#result')
    expect(result_field).to_contain_text('Enter something!')

# RUN: '/udemy/19_continuous_integration/tests
# pytest --headed -v --slowmo=500 '