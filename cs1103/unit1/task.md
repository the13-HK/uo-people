- Discussion Forum

1. How would you explain the purpose and usage of try, catch, throw, and finally blocks in a way that's easy to understand?

   - try、キャッチ、ファイナリー構文は処理を正常に動作させる事を保証するための仕組み作りです。
     プログラミングは処理を事前に定義してその処理を実行するために使用されます。その処理は大抵外側からデータを受け取ってそのデータに対して加工を行い、その結果を返すような処理が多いです。
     そのため、処理を設計、実装する際は想定しているデータを定義する必要がある。また、想定していないデータをどうやって扱うかも定義する必要がある。
     そうしないとシステムエラーとしてプログラミング言語側でエラーを出力するが、他の処理に影響が出たり、システム全体が動かなくなってしまう可能性がある。
     それを防ぐためにも正常に動く場合だけでなく、エラーになった場合の挙動を制御するひつようがある。
     そのために用いられるのが、try, catch, finally である。これらは処理のまとまりを定義する際に使用される、ブロックと一緒に使用され、ブロック構文の先頭に宣言することで使用する。
     次にそれぞれノブロックの特徴を述べていく。

     - try ブロック
       try は宣言することで宣言直後のブロック内でエラーになった際に catch ブロックにジャンプさせることが出来る。
       また、エラーが発生したタイミングで処理は中断され、後続の処理が実行されずにそのまま catch ブロックに遷移する。
       遷移する場合、catch ブロックには throwable クラスを継承しているオブジェクトのみ渡すことが出来る。

     - catch ブロック
       エラーが発生した際の処理を記載することが出来る。もう少し正確にいうと異常が発生した際に throw される throwable クラスを継承したオブジェクトを受取り、それを受け取った時の挙動を定義することが出来る。throwable オブジェクトを受け取らない限りは実行されることがない。受け取ることのできる throwable オブジェクトについても指定をすることが出来る。
       この catch ブロックの中では大抵エラーの記録、出力が主に行われており、エラーの修復なども可能であればおこなわれる。
       例えば、有名な throwable オブジェクトは Exception であり、Exception の中でも IOException や IllegalArgumentException 等が標準的に実装されている Exception である。
       これらは catch ブロックを宣言した直後のカッコで指定することでキャッチする対象のオブジェクトを指定することが出来る。
       例えば下記の catch 文の場合は IOException の場合のみキャッチすることが出来る。
       キャッチする Exception は限定的であればより良い設計とされている。その方がエラーが発生した際に特定が行いやすくなるし、限定的なエラーに特価したエラーハンドリングも行いやすくなるためである。

     ```java
     catch (IOException e) {
        System.out.println(e);
     }
     ```

     - finally ブロック
       finally ブロックは try ブロックと catch ブロックと合わせて使われており、エラーが発生しようとも、必ず処理が実行されることが担保されているブロックである
       そのため、ＤＢの切断処理などのエラー時でも実行しないと他のアプリケーションの動作に影響が発生してしまうような処理を実行させる事が多い。

2. Share practical examples or analogies that can help clarify these concepts for someone with no prior experience in Java.
   - 例えば、スーパーのレジの処理を考えたとしよう。try 文内で実際のレジの計算処理を実行する。買い物の商品の値段を計算して、その合計額を算出し、お金を請求する処理までを実行する。
     もしその処理の中で何らかのエラーが発生してしまった場合、そのエラーの内容に応じて対応をしなけらばならない。だが、それは商品のねだん計算を行っている途中に上手く計算が出来なく手エラーになったときなのか、お金を請求しているときに発生するエラーなのかで対応する内容も異なる。その場合は Exception の種類を変えて、異なる catch ブロック内で拾ってエラーのハンドリングをしなければならない。
     として最後にお客さんから頂いたお金は正しく返却しなければならない。 もし処理がうまくいった場合でも、お釣りは返さなければならないし、エラーが発生して最後まで会計が行われなければ全額請求する必要がある。そういったときは finally 構文内にて返却するべきお金が残っていないかどうかを判定する必要がある。

- English

The try, catch, and finally constructs are mechanisms for ensuring that processing works correctly.
Programming is used to define processing in advance and then execute that processing. Most of this processing involves receiving data from outside, processing that data, and returning the results.
For this reason, when designing and implementing processing, it is necessary to define the expected data. It is also necessary to define how to handle unexpected data.
If this is not done, the programming language will output an error as a system error, which could affect other processes or even cause the entire system to stop working.
To prevent this, it is necessary to control the behavior when an error occurs, not just when things work normally.
These are used for this purpose: try, catch, and finally. These are used together with blocks, which are used to define groups of processes, and are used by declaring them at the beginning of the block syntax.

Next, we will explain the characteristics of each knob block.

- try block
  By declaring try, you can jump to the catch block if an error occurs in the block immediately after the declaration.
  When an error occurs, the process is interrupted and the process transitions to the catch block without executing any subsequent processes.
  When transitioning, only objects that inherit the throwable class can be passed to the catch block.

- catch block
  It allows you to write the processing to be done when an error occurs. More precisely, it receives an object that inherits the throwable class that is thrown when an abnormality occurs, and allows you to define the behavior when it is received. It will not be executed unless a throwable object is received. You can also specify the throwable objects that can be received.
  Inside this catch block, most of the work that is done is recording and outputting errors, and if possible, repairing errors is also done.
  For example, a well-known throwable object is Exception, and among Exceptions, IOException and IllegalArgumentException are some of the Exceptions that are implemented as standard.
  You can specify the object to be caught by specifying it in parentheses immediately after declaring a catch block.
  For example, the following catch statement will only catch IOException.
  It is considered a better design if the Exceptions to be caught are limited. This is because it makes it easier to identify when an error occurs and also makes it easier to handle errors specifically for limited errors.

```java
catch (IOException e) {
System.out.println(e);
}
```

- finally block
  The finally block is used in conjunction with the try block and catch block, and is a block that guarantees that a process will always be executed even if an error occurs.
  For this reason, it is often used to execute processes that, if not executed, would affect the operation of other applications, even in the event of an error, such as a database disconnection process.

2.  For example, let's consider the process of a supermarket cash register. The actual cash register calculation process is carried out within the try statement. The prices of the items purchased are calculated, the total amount is calculated, and the process of charging the money is carried out.
    If an error occurs during this process, a response must be made according to the nature of the error. However, the response will differ depending on whether the error is due to a manual error when calculating the price of the items, or whether the error occurs when charging the money. In that case, you need to change the type of Exception and pick up the error in a different catch block to handle it.
    Then you need to correctly return the money received from the customer. Even if the process is successful, you need to return the change, and if an error occurs and the accounting is not completed, you need to charge the full amount. In such cases, you need to check in the finally statement whether there is any money remaining to be returned.
