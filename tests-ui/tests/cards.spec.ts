import { test, expect } from '@playwright/test';

test('cards smoke via API', async ({ request }) => {
const res = await request.get('http://localhost:8080/cards');
expect(res.status()).toBe(200);
const data = await res.json();
expect(Array.isArray(data)).toBeTruthy();
});