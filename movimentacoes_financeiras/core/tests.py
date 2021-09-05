from collections import namedtuple
from django.test import TestCase
from movimentacoes_financeiras.core.forms import FinancialTransactionsFileForm

TextRepetitions = namedtuple('TextRepetitions', ('text' ,'count'))

class TestMainFormPage(TestCase):
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

    def test_html(self):
        texts_in_html = (
            TextRepetitions(text='<form', count=1),
            TextRepetitions(text='<input', count=2),
            TextRepetitions(text='type="file"', count=1),
            TextRepetitions(text='type="submit"', count=1)
        )
        with self.subTest():
            for text_repetition in texts_in_html:
                self.assertContains(
                    self.response,
                    text_repetition.text,
                    text_repetition.count
                )
