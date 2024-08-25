import 'package:flutter/material.dart';
import 'chat_private_screen.dart';
import 'chat_group_screen.dart';

class HomeScreen extends StatefulWidget {
  @override

  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/home');
              },
              child: Text('Go to Home'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/store');
              },
              child: Text('Go to Store'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/login');
              },
              child: Text('Go to Login'),
            ),
          ],
        ),
      ),
    );
  }
}

class _HomeScreenState extends State<HomeScreen> {
  int _currentIndex = 0;

  final List<Widget> _children = [
    ChatPrivateScreen(),
    ChatGroupScreen(),
  ];

  void _onTabTapped(int index) {
    setState(() {
      _currentIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _children[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: _onTabTapped,
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.chat),
            label: 'Private Chat',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.group),
            label: 'Group Chat',
          ),
        ],
      ),
    );
  }
}
