import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.uic import loadUi
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_distances
from googletrans import Translator


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('login.ui', self)
        self.loginbtn.clicked.connect(self.goto_mainmenu)
        self.createbtn.clicked.connect(self.goto_regis)

    def goto_mainmenu(self):
        if (self.usernameline.text() and self.passwordline.text()) != '':
            mainmenu = MainMenu()
            widget.addWidget(mainmenu)
            widget.setFixedSize(480, 620)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            self.warning.setText("Username atau Password belum diisi")

    def goto_regis(self):
        register = Register()
        widget.addWidget(register)
        widget.setFixedSize(480, 620)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
class Register(QDialog):
    def __init__(self):
        super(Register,self).__init__()
        loadUi('register.ui', self)
        self.registerbtn.clicked.connect(self.regisfn)

    def regisfn(self):
        if (self.usernameline.text() and self.emailline.text()) != '':
            if (self.passwordline.text() == self.confirmpassline.text()):
                login = Login()
                widget.addWidget(login)
                widget.setFixedSize(480, 620)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                self.warning.setText("Password tidak sama")
        else:
            self.warning.setText("Terdapat data yang belum terisi")
        

class MainMenu(QDialog):
    def __init__(self):
        super(MainMenu, self).__init__()
        loadUi('mainmenu.ui', self)
        self.setWindowTitle('Yuk Nonton')
        self.profilebtn.clicked.connect(self.goto_profile)
        self.animebtn.clicked.connect(self.goto_anime)
        self.kdramabtn.clicked.connect(self.goto_kdrama)
        self.moviebtn.clicked.connect(self.goto_movie)
        self.logoutbtn.clicked.connect(self.logout)

    def logout(self):
        login = Login()
        widget.addWidget(login)
        widget.setFixedSize(480, 620)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_profile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setFixedSize(480, 620)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_anime(self):
        anime = Anime()
        widget.addWidget(anime)
        widget.setFixedSize(480, 620)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_kdrama(self):
        kdrama = KDrama()
        widget.addWidget(kdrama)
        widget.setFixedSize(760, 620)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_movie(self):
        movie = Movie()
        widget.addWidget(movie)
        widget.setFixedSize(480, 620)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Anime(QDialog):
    def __init__(self):
        super(Anime, self).__init__()
        loadUi('anime.ui', self)
        self.Sarankan.clicked.connect(self.SarankanClicked)
        self.backbtn.clicked.connect(self.goto_mainmenu)


    def goto_mainmenu(self):
        mainmenu = MainMenu()
        widget.addWidget(mainmenu)
        widget.setFixedSize(480, 620)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def SarankanClicked(self):
        anime_picked = []
        if self.checkBox_1.isChecked():
            anime_picked.append(self.checkBox_1.text())
        if self.checkBox_2.isChecked():
            anime_picked.append(self.checkBox_2.text())
        if self.checkBox_3.isChecked():
            anime_picked.append(self.checkBox_3.text())
        if self.checkBox_4.isChecked():
            anime_picked.append(self.checkBox_4.text())
        if self.checkBox_5.isChecked():
            anime_picked.append(self.checkBox_5.text())
        if self.checkBox_6.isChecked():
            anime_picked.append(self.checkBox_6.text())
        if self.checkBox_7.isChecked():
            anime_picked.append(self.checkBox_7.text())
        if self.checkBox_8.isChecked():
            anime_picked.append(self.checkBox_8.text())
        if self.checkBox_9.isChecked():
            anime_picked.append(self.checkBox_9.text())
        if self.checkBox_10.isChecked():
            anime_picked.append(self.checkBox_10.text())
        if self.checkBox_11.isChecked():
            anime_picked.append(self.checkBox_11.text())
        if self.checkBox_12.isChecked():
            anime_picked.append(self.checkBox_12.text())
        if self.checkBox_13.isChecked():
            anime_picked.append(self.checkBox_13.text())
        if self.checkBox_14.isChecked():
            anime_picked.append(self.checkBox_14.text())
        if self.checkBox_15.isChecked():
            anime_picked.append(self.checkBox_15.text())
        if self.checkBox_16.isChecked():
            anime_picked.append(self.checkBox_16.text())
        if self.checkBox_17.isChecked():
            anime_picked.append(self.checkBox_17.text())
        if self.checkBox_18.isChecked():
            anime_picked.append(self.checkBox_18.text())
        if self.checkBox_19.isChecked():
            anime_picked.append(self.checkBox_19.text())
        if self.checkBox_20.isChecked():
            anime_picked.append(self.checkBox_20.text())
                
        recsys = RecomAnime()
        recom_anime = recsys.recommend(anime_picked)

        self.textEdit.setText("Saya merekomendasikan Anda untuk menonton <b>"+str(recom_anime[0])+
                              "</b> karena Anda sudah menonton "+str(recom_anime[1])+
                              " anime genre "+str(recom_anime[2]))
        

class KDrama(QDialog):
    def __init__(self):
        super(KDrama, self).__init__()
        loadUi('kdrama.ui', self)
        self.recom_kdrama = None
        self.Sarankan.clicked.connect(self.SarankanClicked)
        self.backbtn.clicked.connect(self.goto_mainmenu)


    def goto_mainmenu(self):
        mainmenu = MainMenu()
        widget.addWidget(mainmenu)
        widget.setFixedSize(480, 620)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def SarankanClicked(self):
        kdrama_picked = []
        if self.checkBox_1.isChecked():
            kdrama_picked.append(self.checkBox_1.text())
        if self.checkBox_2.isChecked():
            kdrama_picked.append(self.checkBox_2.text())
        if self.checkBox_3.isChecked():
            kdrama_picked.append(self.checkBox_3.text())
        if self.checkBox_4.isChecked():
            kdrama_picked.append(self.checkBox_4.text())
        if self.checkBox_5.isChecked():
            kdrama_picked.append(self.checkBox_5.text())
        if self.checkBox_6.isChecked():
            kdrama_picked.append(self.checkBox_6.text())
        if self.checkBox_7.isChecked():
            kdrama_picked.append(self.checkBox_7.text())
        if self.checkBox_8.isChecked():
            kdrama_picked.append(self.checkBox_8.text())
        if self.checkBox_9.isChecked():
            kdrama_picked.append(self.checkBox_9.text())
        if self.checkBox_10.isChecked():
            kdrama_picked.append(self.checkBox_10.text())
        if self.checkBox_11.isChecked():
            kdrama_picked.append(self.checkBox_11.text())
        if self.checkBox_12.isChecked():
            kdrama_picked.append(self.checkBox_12.text())
        if self.checkBox_13.isChecked():
            kdrama_picked.append(self.checkBox_13.text())
        if self.checkBox_14.isChecked():
            kdrama_picked.append(self.checkBox_14.text())
        if self.checkBox_15.isChecked():
            kdrama_picked.append(self.checkBox_15.text())
        if self.checkBox_16.isChecked():
            kdrama_picked.append(self.checkBox_16.text())
        if self.checkBox_17.isChecked():
            kdrama_picked.append(self.checkBox_17.text())
        if self.checkBox_18.isChecked():
            kdrama_picked.append(self.checkBox_18.text())
        if self.checkBox_19.isChecked():
            kdrama_picked.append(self.checkBox_19.text())
        if self.checkBox_20.isChecked():
            kdrama_picked.append(self.checkBox_20.text())

        recsys = RecomKdrama()
        recsys.fit()
        self.recom_kdrama = recsys.recommend(kdrama_picked)

        self.textEdit.setText("Saya merekomendasikan Anda untuk menonton <b>"+str(self.recom_kdrama['Title'].to_list())+
                              "</b> berdasarkan alur cerita drama korea yang Anda tonton sebelumnya")
        
        translator = Translator()
        detail_kdrama = ''
        for i in range(len(self.recom_kdrama)):
            translation = translator.translate(self.recom_kdrama['Synopsis'][i],dest='id',scr='en')
            detail_kdrama = detail_kdrama + '<b>'+str(self.recom_kdrama['Title'][i])+'</b> '+translation.text+'<br><br>'

        self.textBrowser.setText(detail_kdrama)


class Movie(QDialog):
    def __init__(self):
        super(Movie, self).__init__()
        loadUi('box_office.ui', self)
        self.progressBar.setValue(0)
        self.Sarankan.clicked.connect(self.SarankanClicked)
        self.backbtn.clicked.connect(self.goto_mainmenu)


    def goto_mainmenu(self):
        mainmenu = MainMenu()
        widget.addWidget(mainmenu)
        widget.setFixedSize(480, 620)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def SarankanClicked(self):
        movie_picked = []
        if self.checkBox_1.isChecked():
            movie_picked.append(self.checkBox_1.text())
        if self.checkBox_2.isChecked():
            movie_picked.append(self.checkBox_2.text())
        if self.checkBox_3.isChecked():
            movie_picked.append(self.checkBox_3.text())
        if self.checkBox_4.isChecked():
            movie_picked.append(self.checkBox_4.text())
        if self.checkBox_5.isChecked():
            movie_picked.append(self.checkBox_5.text())
        if self.checkBox_6.isChecked():
            movie_picked.append(self.checkBox_6.text())
        if self.checkBox_7.isChecked():
            movie_picked.append(self.checkBox_7.text())
        if self.checkBox_8.isChecked():
            movie_picked.append(self.checkBox_8.text())
        if self.checkBox_9.isChecked():
            movie_picked.append(self.checkBox_9.text())
        if self.checkBox_10.isChecked():
            movie_picked.append(self.checkBox_10.text())
        if self.checkBox_11.isChecked():
            movie_picked.append(self.checkBox_11.text())
        if self.checkBox_12.isChecked():
            movie_picked.append(self.checkBox_12.text())
        if self.checkBox_13.isChecked():
            movie_picked.append(self.checkBox_13.text())
        if self.checkBox_14.isChecked():
            movie_picked.append(self.checkBox_14.text())
        if self.checkBox_15.isChecked():
            movie_picked.append(self.checkBox_15.text())
        if self.checkBox_16.isChecked():
            movie_picked.append(self.checkBox_16.text())
        if self.checkBox_17.isChecked():
            movie_picked.append(self.checkBox_17.text())
        if self.checkBox_18.isChecked():
            movie_picked.append(self.checkBox_18.text())
        if self.checkBox_19.isChecked():
            movie_picked.append(self.checkBox_19.text())
        if self.checkBox_20.isChecked():
            movie_picked.append(self.checkBox_20.text())

        recsys = RecomMovie()
        self.progressBar.setValue(15)
        recsys.fit()
        recom_movie = recsys.recommend(movie_picked)

        self.textEdit.setText("Saya merekomendasikan Anda untuk menonton <b>"+str(recom_movie)+
                              "</b>.")
        self.progressBar.setValue(100)


        

class Profile(QDialog):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi('profile.ui', self)
        self.backbtn.clicked.connect(self.goto_mainmenu)


    def goto_mainmenu(self):
        mainmenu = MainMenu()
        widget.addWidget(mainmenu)
        widget.setFixedSize(480, 620)
        widget.setCurrentIndex(widget.currentIndex()+1)

class RecomAnime:
    def __init__(self):
        self.df_anime = pd.read_csv('Anime Genres for 20.csv')
        
    def recommend(self, anime_picked):
        pick_data = self.df_anime[self.df_anime['Title'].isin(anime_picked)] #data anime terpilih
        sum_of_columns = pick_data.select_dtypes(include='number').sum() 
        recom_sum = sum_of_columns.max()
        recom_genre = sum_of_columns.idxmax() # genre paling sering ditonton
        recom_anime = self.df_anime['Title'][self.df_anime[recom_genre]==1].to_list()

        for elemen in anime_picked:
            if elemen in recom_anime:
                recom_anime.remove(elemen)

        if (len(recom_anime)>3):
            recom_anime = recom_anime[:3]

        return [recom_anime, recom_sum, recom_genre]
    
class RecomKdrama:
    def __init__(self):
        self.df_kdrama = pd.read_csv('Korean Drama Synopsis 20.csv')
        self.encoder = None
        self.bank_kdrama = None

    def fit(self):
        self.encoder = CountVectorizer(stop_words='english', tokenizer=word_tokenize)
        self.bank_kdrama = self.encoder.fit_transform(self.df_kdrama['Synopsis'])

    def recommend(self, kdrama_picked):
        pick_idx = self.df_kdrama.index[self.df_kdrama['Title'].isin(kdrama_picked)].to_list()
        content = ''
        for i in range(len(pick_idx)):
            content = content + self.df_kdrama.loc[pick_idx[i], 'Synopsis'] + ' '
        code = self.encoder.transform([content])
        dist = cosine_distances(code, self.bank_kdrama)
        rec_idx = dist.argsort()[0, 0:len(kdrama_picked)+3]
        print(rec_idx)
        for idx in pick_idx:
            if idx in rec_idx:
                rec_idx = rec_idx[rec_idx != idx]
        rec_data = self.df_kdrama.loc[rec_idx]
        rec_data = rec_data.reset_index(drop=True)

        return rec_data
    
class RecomMovie:
    def __init__(self):
        self.df_movie = pd.read_csv('Box Office 500.csv')
        self.encoder = None
        self.bank_movie = None

    def fit(self):
        self.encoder = CountVectorizer(stop_words='english', tokenizer=word_tokenize)
        self.bank_movie = self.encoder.fit_transform(self.df_movie['metadata'])
        #progressbar.setValue(80)

    def recommend(self, movie_picked):
        pick_idx = self.df_movie.index[self.df_movie['title'].isin(movie_picked)].to_list()
        content = ''
        for i in range(len(pick_idx)):
            content = content + self.df_movie.loc[pick_idx[i], 'metadata'] + ' '
        code = self.encoder.transform([content])
        dist = cosine_distances(code, self.bank_movie)
        rec_idx = dist.argsort()[0, 0:len(movie_picked)+3]
        print(rec_idx)
        for idx in pick_idx:
            if idx in rec_idx:
                rec_idx = rec_idx[rec_idx != idx]
        rec_data = self.df_movie.loc[rec_idx]
        rec_title = rec_data['title'].to_list()


        return rec_title


            




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.setFixedSize(480, 620)
    widget.show()
    app.exec_()