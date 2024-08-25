import 'package:flutter/material.dart';
import 'package:flutter_windowmanager/flutter_windowmanager.dart';
import 'screens/login_screen.dart';
import 'screens/home_screen.dart';
import 'screens/store_screen.dart';
//import 'package:meu_plugin/meu_plugin.dart';


void main() {
  WidgetsFlutterBinding.ensureInitialized();
  FlutterWindowManager.addFlags(FlutterWindowManager.FLAG_SECURE);
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Secure Messenger',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => SplashScreen(),
        '/login': (context) => LoginScreen(),
        '/home': (context) => HomeScreen(),
        '/store': (context) => StoreScreen(),
      },
    );
  }
}

class SplashScreen extends StatefulWidget {
  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    _navigateToNextScreen();
  }

  void _navigateToNextScreen() async {
    // Simulate a delay for splash screen
    await Future.delayed(Duration(seconds: 3));
    // Navigate to login screen (or any other logic you need)
    Navigator.of(context).pushReplacementNamed('/login');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset('assets/logo.png'), // Your logo asset
            SizedBox(height: 20),
            ProgressIndicatorWidget(), // Custom progress indicator
          ],
        ),
      ),
    );
  }
}