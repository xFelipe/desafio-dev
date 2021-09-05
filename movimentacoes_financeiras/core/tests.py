from django.test import TestCase
from movimentacoes_financeiras.core.forms import FinancialTransactionsFileForm

class TestMainPage(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get_main_page_has_status_code_200(self):
        self.assertEquals(200, self.response.status_code)

    def test_get_main_page_template(self):
        template = 'financial_transactions.html'
        self.assertTemplateUsed(self.response, template)

    def test_get_main_page_title(self):
        espected_title = 'Inserir movimentações financeiras'
        tag_title = f'<title>{espected_title}</title>'
        self.assertContains(
            self.response,
            tag_title
        )

    def test_has_form(self):
        """Context must have FinancialTransactions form"""
        self.assertIsInstance(
            self.response.context['form'],
            FinancialTransactionsFileForm
        )
