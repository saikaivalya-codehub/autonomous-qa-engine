PROMPT_PATH = "agent/prompts/testgen_prompt.md"

def generate_tests_from_story(title: str, text: str):
    # Simple heuristic: extract endpoints & actions; produce Gherkin + Playwright
    gherkin = f"""Feature: {title}\n  As a user, I want {title} so that value is delivered\n\n  Scenario: Happy path\n    Given the service is running\n    When I GET /cards\n    Then I receive 200 and a non-empty list\n\n  Scenario: Create and adjust limit\n    When I POST /cards with body {{\"holder\":\"Alice\",\"limit\":1000}}\n    Then status 201 and id is returned\n    When I PATCH /cards/{{id}}/limit with body {{\"limit\":1500}}\n    Then status 200 and limit is 1500\n"""
    playwright = """import { test, expect } from '@playwright/test';\n\ntest('cards smoke', async ({ request }) => {\n  const list = await request.get('http://localhost:8080/cards');\n  expect(list.status()).toBe(200);\n  const data = await list.json();\n  expect(Array.isArray(data)).toBeTruthy();\n});\n"""
    return gherkin, playwright