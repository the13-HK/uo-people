#### Generic class in java
### Discussion Questions
a) When designing generic classes and methods, what factors do you prioritize to ensure flexibility and maintainability? 
柔軟性と保守性を確保するためにはジェネリッククラスを使用する事を心がけることが重要である。
まず、ジェネリッククラスはクラスやメソッドで扱う型をパラメータとして受け取るようにすることである。サンプルコードは下記の通りである。

```java
public class GenericClass<T> {
    private T value;

    public GenericClass(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        this.value = value;
    }
}
```
ジェネリックでは型を鍵カッコで囲むことで、クラスやメソッドで扱う型をパラメータとして受け取ることができる。
パラメータとして受け取らない場合、各クラスで扱える型は固定となってしまうため、柔軟性が失われてしまう。
もし同じような処理をString型とInteger型で行う場合、String型とInteger型それぞれにクラスを作成する必要がある。
また、もしどんな変数でも扱えるように文字型の指定をしない場合は、保守性が失われ、エラーが発生しやすくなるだけでなく、可読性も失われてしまう。
操作するメソッドの共通化をどこまで行うかについての設計は重要ではあるが、共通化されたメソッドを使用することで、コードの重複を減らし、保守性を向上させることができる。

b) Share any challenges or roadblocks you faced when implementing generics. How did you overcome these challenges? 
共通の継承元を持つ型を扱う場合のジェネリックの指定方法を把握していると今後の開発や設計で役立つを思うのでシェアをします。
下記のような書き方をすることでNumber型を継承したクラスを指定することができる。
これはJavaのデフォルトの文字型をのみを扱う場合では大きなメリットは得られないが、大規模なアプリケーションにおいて独自の型を定義している場合は、共通の継承元を持つ型を扱うことで、コードの重複を減らし、保守性を向上させることができる。
```java
public class GenericClass<T extends Number> {
    private T value;

    public GenericClass(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        this.value = value;
    }
}
```

例えば、あなたは商品の値段に対して操作を行うクラスを作成したいとします。ねだんの操作はいくつかあり、値引きをする、消費税を計算する、などの操作があるとします。
その場合、値段はNumber型を継承したクラスである必要があります。なぜなら、値引きや消費税の計算は数値に対して行う操作だからです。
その場合、下記のようにNumber型を継承したクラスを指定することができます。
```java
public class DiscountCalculator<T extends Number> {
    private T price;

    public DiscountCalculator(T price) {
        this.price = price;
    }

    public T getPrice() {
        return price;
    }

    public void setPrice(T price) {
        this.price = price;
    }

    // Calculate discount
    public double applyDiscount(double discountRate) {
        if (discountRate < 0 || discountRate > 1) {
            throw new IllegalArgumentException("Please specify a discount rate between 0 and 1.");
        }
        return price.doubleValue() * (1 - discountRate);
    }
}
``
```java
public class TaxCalculator<T extends Number> {
    private T price;

    public TaxCalculator(T price) {
        this.price = price;
    }

    public T getPrice() {
        return price;
    }

    public void setPrice(T price) {
        this.price = price;
    }

    // Calculate tax
    public double calculateTax(double taxRate) {
        if (taxRate < 0) {
            throw new IllegalArgumentException("Please specify a tax rate greater than or equal to 0.");
        }
        return price.doubleValue() * taxRate;
    }
}
```