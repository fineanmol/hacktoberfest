import 'package:bookswap_flutter/constants.dart';
import 'package:bookswap_flutter/methods/custom_button.dart';
import 'package:bookswap_flutter/screens/forgot_password_screen.dart';
import 'package:bookswap_flutter/screens/sign_up_screen.dart';
import 'package:flutter/material.dart';

class SignInScreen extends StatefulWidget {
  static const id = 'signInScreen';
  @override
  _SignInScreenState createState() => _SignInScreenState();
}

class _SignInScreenState extends State<SignInScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Expanded(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Hero(
                    tag: 'logo',
                    child: Container(
                      child: Image.asset(kLogoPath),
                    ),
                  ),
                  TextField(
                    keyboardType: TextInputType.emailAddress,
                    onChanged: (value) {
                      print(value);
                    },
                    decoration:
                        kTextFieldDecoration.copyWith(hintText: 'Email'),
                  ),
                  SizedBox(
                    height: 8,
                  ),
                  TextField(
                    obscureText: true,
                    onChanged: (value) {
                      print(value);
                    },
                    decoration:
                        kTextFieldDecoration.copyWith(hintText: 'Password'),
                  ),
                  SizedBox(
                    height: 8,
                  ),
                  Align(
                    alignment: Alignment.centerRight,
                    child: GestureDetector(
                      child: Text(
                        'Forgot Password?',
                        style: kForgotPasswordTextStyle,
                      ),
                      onTap: () {
                        print('Tapped ForgotPassword');
                        Navigator.pushNamed(context, ForgotPassword.id);
                      },
                    ),
                  ),
                  CustomButton(
                    text: 'Sign In',
                    onPressed: () {
                      print('Button Pressed');
                    },
                  ),
                ],
              ),
            ),
            SignUpRow(),
          ],
        ),
      ),
    );
  }
}

class SignUpRow extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(
        bottom: 30,
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            "Don't have an account?",
          ),
          SizedBox(
            width: 8,
          ),
          GestureDetector(
            onTap: () {
              // print('SignUpTapped');
              Navigator.pushNamed(context, SignUpScreen.id);
            },
            child: Text(
              'Sign Up',
              style: kSignUpTextStyle,
            ),
          ),
        ],
      ),
    );
  }
}
