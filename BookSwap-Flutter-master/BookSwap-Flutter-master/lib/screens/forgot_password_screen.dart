import 'package:bookswap_flutter/constants.dart';
import 'package:bookswap_flutter/methods/custom_button.dart';
import 'package:bookswap_flutter/screens/sign_in_screen.dart';
import 'package:flutter/material.dart';

class ForgotPassword extends StatefulWidget {
  static const id = 'forgotPasswordScreen';
  @override
  _ForgotPasswordState createState() => _ForgotPasswordState();
}

class _ForgotPasswordState extends State<ForgotPassword> {
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
                    decoration: kTextFieldDecoration.copyWith(
                      hintText: 'Email',
                    ),
                    onChanged: (value) {
                      print(value);
                    },
                  ),
                  SizedBox(
                    height: 8,
                  ),
                  CustomButton(
                    text: 'Reset Password',
                    onPressed: () {
                      print('pressed resetButton');
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
