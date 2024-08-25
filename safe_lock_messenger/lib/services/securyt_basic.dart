import 'dart:math';

// Função para simular 2 qubits
List<int> simulateQubits(Random random) {
  int qubit1 = random.nextInt(2);
  int qubit2 = random.nextInt(2);
  return [qubit1, qubit2];
}

// Função para simular um sistema estelar de 3 corpos e um invasor
List<List<double>> simulateStellarSystem(Random random) {
  List<double> body1 = [random.nextDouble(), random.nextDouble()];
  List<double> body2 = [random.nextDouble(), random.nextDouble()];
  List<double> body3 = [random.nextDouble(), random.nextDouble()];
  List<double> invader = [random.nextDouble(), random.nextDouble()];
  return [body1, body2, body3, invader];
}

// Função para simular a demolição de ondas quânticas
List<double> simulateQuantumWaveDemolition(Random random) {
  double amplitude = random.nextDouble();
  double frequency = random.nextDouble();
  // Simula a demolição
  amplitude *= 0.5;
  frequency *= 0.5;
  return [amplitude, frequency];
}

// Função para simular o afunilamento de ondas quânticas e criação de corpos quânticos
double simulateQuantumBody(Random random) {
  double density = random.nextDouble();
  double energy = random.nextDouble();
  return density * energy; // massa do corpo quântico
}

// Função para gerar uma string de caracteres aleatórios
String generateRandomString(int length) {
  const chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
  final random = Random();
  return List.generate(length, (index) => chars[random.nextInt(chars.length)]).join();
}

// Função para testar a resistência de uma senha
bool isPasswordResistant(String password, List<int> qubits) {
  int qubitSum = qubits.reduce((a, b) => a + b);
  int resistanceFactor = qubitSum + password.length;
  // Critério mais complexo para resistência da senha
  return resistanceFactor > 20 && password.length >= 8;
}

void main() {
  final random = Random();

  // 1. Simulação de 2 Qubits
  List<int> qubits = simulateQubits(random);
  print('Qubit 1: ${qubits[0]}');
  print('Qubit 2: ${qubits[1]}');

  // 2. Sistema Estelar de 3 Corpos com um Invasor Aleatório
  List<List<double>> stellarSystem = simulateStellarSystem(random);
  print('Sistema Estelar:');
  print('Corpo 1: (${stellarSystem[0][0]}, ${stellarSystem[0][1]})');
  print('Corpo 2: (${stellarSystem[1][0]}, ${stellarSystem[1][1]})');
  print('Corpo 3: (${stellarSystem[2][0]}, ${stellarSystem[2][1]})');
  print('Invasor: (${stellarSystem[3][0]}, ${stellarSystem[3][1]})');

  // 3. Demolição de Ondas Quânticas
  List<double> waveData = simulateQuantumWaveDemolition(random);
  print('Onda Quântica após Demolição:');
  print('Amplitude: ${waveData[0]}');
  print('Frequência: ${waveData[1]}');

  // 4. Afinamento de Ondas Quânticas e Criação de Corpos Quânticos
  double quantumBody = simulateQuantumBody(random);
  print('Corpo Quântico Criado:');
  print('Massa: $quantumBody');

  // 5. Geração de Caracteres Aleatórios
  String randomString = generateRandomString(10);
  print('Caracteres Aleatórios: $randomString');

  // Teste de Resistência de Senha
  String password = 'example_password'; // Senha a ser testada
  bool isResistant = isPasswordResistant(password, qubits);
  print('A senha "$password" é ${isResistant ? 'resistente' : 'não resistente'}.');
}