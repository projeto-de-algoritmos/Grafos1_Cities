from metaflow import (
        FlowSpec,
        step,
        IncludeFile,
        Parameter)

class TouristPreProcessing(FlowSpec):
    @step
    def start(self):
        import pandas as pd
        self.df_border = pd.read_csv("./data/border_info.csv")
        self.df_continents = pd.read_csv("./data/countries.csv")
        self.df_border = self.df_border.sort_values(by=['country_name'])
        self.df_continents = self.df_continents.sort_values(by=['Country'])
        self.next(self.clean_border_data)
    
    @step
    def clean_border_data(self):
        is_NaN = self.df_border.isnull()
        row_has_NaN = is_NaN.any(axis=1)
        rows_with_NaN = self.df_border[row_has_NaN]
        self.df_border = self.df_border.drop(rows_with_NaN.index)
        self.next(self.list_convertion)

    @step
    def list_convertion(self):
        k = self.df_border.groupby('country_name')['country_border_name'].apply(lambda x: list(x))
        self.df_border = self.df_border.drop(columns=['country_border_name'])
        self.df_border = self.df_border.drop_duplicates(subset=['country_name'])
        aux = [item for item in k]
        self.df_border['border_list'] = aux
        self.df_border = self.df_border.reset_index()
        self.df_border = self.df_border.drop(columns=['Unnamed: 0', 'index'])
        self.next(self.data_crossing)

    @step
    def data_crossing(self):
        self.df_continents['Region'] = self.df_continents['Region'].replace('LATIN', 'AMERICA')
        self.df_continents['Region'] = self.df_continents['Region'].replace('NORTHERN_AMERICA', 'AMERICA')
        self.df_continents['Region'] = self.df_continents['Region'].replace('NEAR_EAST', 'ASIA')
        border_l = self.df_border['country_name'].tolist()
        cont_l = self.df_continents['Country'].tolist()
        diff = []
        for item in cont_l:
            if item in border_l:
                continent = self.df_continents.loc[self.df_continents['Country'] == item]
                continent = continent['Region']
                for elem in continent.iteritems():
                    self.df_border.loc[self.df_border['country_name'] == item, 'continent'] = elem[1]
        self.next(self.fill_continent_country_null_data)

    @step
    def fill_continent_country_null_data(self):
        eu = ['Bosnia and Herzegovina', 'Czechia', 'Holy See', 'Montenegro', 'North Macedonia']
        asia = ['Korea (Democratic People\'s Republic of)', 'Korea, South', 'Macao', 'Myanmar', 'Palestine, State of', 'Timor-Leste']
        america = ['Saint Martin (French part)', 'Sint Maarten (Dutch part)', 'US']
        africa = ['Central African Republic', 'Congo (Kinshasa)', 'Congo (the Democratic Republic of the)', 'Cote d\'Ivoire', 'Eswatini', 'South Africa', 'South Sudan']
        for country in eu:
            self.df_border.loc[self.df_border['country_name'] == country, 'continent'] = 'EUROPE'
        for country in asia:
            self.df_border.loc[self.df_border['country_name'] == country, 'continent'] = 'ASIA'
        for country in america:
            self.df_border.loc[self.df_border['country_name'] == country, 'continent'] = 'AMERICA'
        for country in africa:
            self.df_border.loc[self.df_border['country_name'] == country, 'continent'] = 'AFRICA'
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    TouristPreProcessing()