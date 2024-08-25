import io.flutter.embedding.engine.plugins.FlutterPlugin;
import io.flutter.plugin.common.MethodCall;
import io.flutter.plugin.common.MethodChannel;

public class MeuPlugin implements FlutterPlugin {
  private MethodChannel channel;

  @Override
  public void onAttachedToEngine(FlutterPluginBinding binding) {
    channel = new MethodChannel(binding.getFlutterEngine().getDartExecutor(), "meu_plugin");
    channel.setMethodCallHandler(this);
  }

  @Override
  public void onDetachedFromEngine(FlutterPluginBinding binding) {
    channel.setMethodCallHandler(null);
  }

  @Override
  public void onMethodCall(MethodCall call, Result result) {
    if (call.method.equals("chamarAplicativoTypeScript")) {
      // Chame o aplicativo TypeScript aqui
      String resultado = chamarAplicativoTypeScript();
      result.success(resultado);
    } else {
      result.notImplemented();
    }
  }

  private String chamarAplicativoTypeScript() {
    // Chame o aplicativo TypeScript aqui
    // ...
    /safe_lock_messenger/blockchain
    return "Resultado do aplicativo TypeScript";
  }
}