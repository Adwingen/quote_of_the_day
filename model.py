#model.py


import pandas as pd


class DataModel:
    def __init__(self):
        self.quote_random = None
        self.df = None
        self.used_quotes = None
        self.unused_quotes = None
        self.data_file_quotes = "quotes.txt"
        self.data_file_used_quotes = "used_quotes.csv"

        self.load_data()

    def load_data(self):
        """Carrega as citações e as organiza em DataFrames."""
        # Carrega as citações do arquivo
        with open(self.data_file_quotes, "r") as data_file:
            quotes = data_file.readlines()

        # Limpeza e separação dos dados
        quotes_cleaned = [line.strip() for line in quotes if line.strip()]
        authors = [quote.split(" - ")[-1] for quote in quotes_cleaned]
        quotes_text = [" - ".join(quote.split(" - ")[:-1]) for quote in quotes_cleaned]

        # Cria o DataFrame principal
        self.df = pd.DataFrame({"Quote": quotes_text, "Author": authors})

        # Carrega citações já usadas ou cria um DataFrame vazio
        try:
            self.used_quotes = pd.read_csv(self.data_file_used_quotes)
        except FileNotFoundError:
            self.used_quotes = pd.DataFrame(columns=self.df.columns)

        # Filtra as citações não usadas
        self.unused_quotes = self.df[~self.df['Quote'].isin(self.used_quotes['Quote'])]

    def select_random_quote(self):
        """Seleciona uma citação aleatória e a marca como usada."""
        if not self.unused_quotes.empty:
            self.quote_random = self.unused_quotes.sample(n=1)
            quote_text = self.quote_random['Quote'].values[0]
            author = self.quote_random['Author'].values[0]

            # Atualiza a lista de usadas e salva
            self.used_quotes = pd.concat([self.used_quotes, self.quote_random])
            self.used_quotes.to_csv(self.data_file_used_quotes, index=False)

            return quote_text, author
        else:
            return None, None

