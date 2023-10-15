import 'package:bookswap_flutter/constants.dart';
import 'package:bookswap_flutter/methods/custom_button.dart';
import 'package:flutter/material.dart';

class SignUpScreen extends StatefulWidget {
  static const id = 'signUpScreen';
  @override
  _SignUpScreenState createState() => _SignUpScreenState();
}

class _SignUpScreenState extends State<SignUpScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 20),
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
              decoration: kTextFieldDecoration.copyWith(
                hintText: 'Username',
              ),
            ),
            SizedBox(
              height: 8,
            ),
            TextField(
              decoration: kTextFieldDecoration.copyWith(
                hintText: 'Email',
              ),
              keyboardType: TextInputType.emailAddress,
            ),
            SizedBox(
              height: 8,
            ),
            TextField(
              decoration: kTextFieldDecoration.copyWith(
                hintText: 'Password',
              ),
              obscureText: true,
            ),
            SizedBox(
              height: 8,
            ),
            TextField(
              decoration: kTextFieldDecoration.copyWith(
                hintText: 'Confirm Password',
              ),
              obscureText: true,
            ),
            SizedBox(
              height: 8,
            ),
            CustomButton(
              text: 'Sign Up',
              onPressed: () {
                print('sign up pressed');
              },
            ),
          ],
        ),
      ),
    );
  }
}
