import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          title: Text(
            "Hello, World",
          ),
        ),
        body: SafeArea(
          child: Center(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  'Hello, World',
                  style: TextStyle(
                    color: Colors.blue,
                    fontSize: 80.0,
                  ),
                ),
                SizedBox(
                  width: double.infinity,
                  height: 20.0,
                ),
                Text(
                  "~ Kunal Kumar Sahoo",
                  style: TextStyle(fontSize: 28.0),
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
