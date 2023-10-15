import 'package:flutter/material.dart';

// app theme

final kAppTheme = ThemeData.dark().copyWith(
  primaryColor: Color(0xff1b1b27),
  scaffoldBackgroundColor: Color(0xff2c2c36),
  buttonColor: Color(0xfff88801),
  textTheme: TextTheme(),
);

// Text field decoration (sign in, sign up, forgot password)
const kTextFieldDecoration = InputDecoration(
  hintText: 'Enter value',
  contentPadding: EdgeInsets.symmetric(vertical: 10.0, horizontal: 20.0),
  border: OutlineInputBorder(
    borderRadius: BorderRadius.all(Radius.circular(32.0)),
  ),
  enabledBorder: OutlineInputBorder(
    borderSide: BorderSide(color: Colors.grey, width: 1.0),
    borderRadius: BorderRadius.all(Radius.circular(32.0)),
  ),
  focusedBorder: OutlineInputBorder(
    borderSide: BorderSide(color: Colors.grey, width: 2.0),
    borderRadius: BorderRadius.all(Radius.circular(32.0)),
  ),
);

// text styles
const kForgotPasswordTextStyle = TextStyle(
  color: Colors.lightBlueAccent,
);

final kSignUpTextStyle = TextStyle(
  fontSize: 20,
  color: kAppTheme.buttonColor,
);

// logo path
const kLogoPath = "images/logo.png";
