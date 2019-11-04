import Post from './source/components/post';

import React from 'react';

import {
  SafeAreaView,
  StyleSheet,
  ScrollView,
  FlatList,
  View,
  Text,
  StatusBar,
} from 'react-native';

import {
  Header,
  LearnMoreLinks,
  Colors,
  DebugInstructions,
  ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';

function paginaInicial() {


  return(

    <ScrollView style={styles.scrollView}>


        <Post name = 'Joana - Administradora' username = 'joana.admin'  />
        <Post name = 'Fernanda Lopes' username = 'fernanda.lopes' />
        <Post name = 'Julia Teixeira' username = 'julia.teixeira' />
        <Post name = 'Marcio Sousa' username = 'marcio.sousa' />
        <Post name = 'Ricardo Freitas' username = 'ricardo.freitas' />
        <Post name = 'Henrique Ribeiro' username = 'henrique.ribeiro' />
        <Post name = 'Juliano Prestes' username = 'juliano.prestes'  />
        <Post name = 'Deyse Lima' username = 'deyse.lima' />
        <Post name = 'Carlos Rodrigues' username = 'carlos.rodrigues' />
        <Post name = 'Thiago Queiroz' username = 'thiago.queiroz'  />
        <Post name = 'Domingos Ferreira' username = 'domingos.ferreira' />
        <Post name = 'Karla Marques' username = 'karla.marques' />
      
    </ScrollView>

    

  )

}



const styles = StyleSheet.create(
{
  scrollView : {
    backgroundColor: Colors.lighter,
  },
  engine : {
    position :'absolute',
    right : 0,
  },
  body : {
    backgroundColor : Colors.white,
  },
  sectionContainer : {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle : {
    fontSize: 24,
    fontWeight: '600',
    color: Colors.black,
  },
  sectionDescription : {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
    color: Colors.dark,
  },
  highlight: {
    fontWeight: '700',
  },
  footer: {
    color: Colors.dark,
    fontSize: 12,
    fontWeight: '600',
    padding: 4,
    paddingRight: 12,
    textAlign: 'right',
  }
} );

export default paginaInicial;

