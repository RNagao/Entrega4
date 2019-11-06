import React from 'react';
import { View, StyleSheet, Text, Image } from 'react-native';
import { screenWidth, screenHeight } from '../../constants';
import PropTypes from 'prop-types';
import { SSL_OP_TLS_ROLLBACK_BUG } from 'constants';



export default function Post(props) {
  return (

    <View style={{flexDirection: 'row',borderBottomColor:'#bfc7c1', borderBottomWidth:1, paddingTop:5, backgroundColor:props.backgroundcolor}}>
        <View style= {{backgroundColor:props.backgroundcolor, width:screenWidth * 0.2,paddingTop:screenHeight * 0.01}}>
        </View>
            <View style ={[styles.post, {backgroundColor:props.backgroundcolor}]}>
                <View style ={{flexDirection:'row'}}>
                    <Text style ={{fontWeight:'bold', color:props.textcolor}}>
                        {props.name}
                    </Text>
                    <Text style ={{color:'grey'}}>
                        {'@' + props.username}
                    </Text>
                </View>
                <Text style ={[styles.texto, {color:props.textcolor}]}>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada leo nulla, sit amet volu 
                </Text>
            </View>
    </View>
  );
}


const styles = StyleSheet.create({

    container:{
        flexDirection:'row'


    },

    post:{
        alignSelf:"flex-end",
        width: screenWidth * 0.8,
        marginBottom: screenHeight * 0.02 ,
        alignContent:'center',
      //  backgroundColor:'blue',
        borderRadius: 2,
    },

    postContainer:{
        margin: 20,
        padding: 20,
        backgroundColor: "#CECCCC",
        borderRadius: 5,
    }


})

Post.propTypes ={
    username: PropTypes.string.isRequired,
   // fontColor: PropTypes.string.isRequired
  }