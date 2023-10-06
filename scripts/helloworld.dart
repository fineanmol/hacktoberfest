void main() {
runApp(const GeeksForGeeks());
}

class GeeksForGeeks extends StatelessWidget {
const GeeksForGeeks({Key? key}) : super(key: key);

@override
Widget build(BuildContext context) {
	return const MaterialApp(
	home: Center(child: Text('Hello World')),
	);
}
}
