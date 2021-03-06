## 出错页解析
在页面顶部，你可以得到关键的异常信息： 异常数据类型、异常的参数 、在哪个文件中引发了异常、出错的行号等等。

在关键异常信息下方，该页面显示了对该异常的完整 Python 追踪信息。 这类似于你在 Python 命令行解释器中获得的追溯信息，只不过后者更具交互性。 对栈中的每一帧，Django 均显示了其文件名、函数或方法名、行号及该行源代码。

点击该行代码 (以深灰色显示)，你可以看到出错行的前后几行，从而得知相关上下文情况。

点击栈中的任何一帧的“Local vars”可以看到一个所有局部变量的列表，以及在出错 那一帧时它们的值。 这些调试信息相当有用。

注意“Traceback”下面的“Switch to copy-and-paste view”文字。 点击这些字，追溯会 切换另一个视图，它让你很容易地复制和粘贴这些内容。 当你想同其他人分享这些异常 追溯以获得技术支持时（比如在 Django 的 IRC 聊天室或邮件列表中），可以使用它。

你按一下下面的“Share this traceback on a public Web site”按钮，它将会完成这项工作。 点击它以传回追溯信息至http://www.dpaste.com/，在那里你可以得到一个单独的URL并与其他人分享你的追溯信息。

接下来的“Request information”部分包含了有关产生错误的 Web 请求的大量信息： GET 和 POST、cookie 值、元数据（象 CGI 头）。 在附录H里给出了request的对象的 完整参考。

Request信息的下面，“Settings”列出了 Django 使用的具体配置信息。 （我们已经提及过ROOT_URLCONF，接下来我们将向你展示各式的Django设置。 附录D覆盖了所有可用的设置。）

## 将你从print打印中解放出来

不知道你是不是那种使用小心放置的 print 语句来帮助调试的程序员？ 你其实可以用 Django 出错页来做这些，而不用 print 语句。 在你视图的任何位置，临时插入一个 assert False 来触发出错页。 然后，你就可以看到局部变量和程序语句了