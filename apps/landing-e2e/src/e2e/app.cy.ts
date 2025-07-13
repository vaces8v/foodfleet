import { getGreeting } from '../support/app.po';

describe('landing', () => {
  beforeEach(() => cy.visit('/'));

  it('should display welcome message', () => {
    getGreeting().contains('Welcome landing');
  });
});
