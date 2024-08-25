package app.safe_lock.secure_messenger;

public class ChaosTree {

    private double[] state;

    public ChaosTree(int size) {
        state = new double[size];
        // Inicializar o estado com valores aleatórios
        for (int i = 0; i < size; i++) {
            state[i] = Math.random();
        }
    }

    public void iterate() {
        // Atualizar o estado do sistema de caos
        // Exemplo simples
        for (int i = 0; i < state.length; i++) {
            state[i] = (state[i] * 2) % 1;
        }
    }

    public double[] getState() {
        return state;
    }
}
