---
title: js中几种设计模式
catalog: true
date: 2019-07-14 21:50:10
subtitle:
header-img:
tags: javascript
---

1. 工厂模式

> TODO

```javascript
class Product  {
    constructor (name) {
        this.name = name
    }
}

class Creator {
    create (name) {
        return new Product(name)
    }
}

const creatorInstance = new Creator()

creatorInstance.create('张三')
```

应用场景：TODO

2. 单例模式

> 一个类只有一个实例，并提供全局访问的方法，一般用于登录、购物车等场景

```javascript
class Single {
    login () {}
    shopping () {}
}

Single.getInstance = (function () {
    let Instance
    return () => {
        if (!Instance) {
                Instance = new Single()
        }
        return Instance
    }
})()

const signleInstanceA = Single.getInstance()
const signleInstanceB = Single.getInstance()
console.log(signleInstanceA === signleInstanceB) // true
```

应用场景：TODO

3. 适配器模式

> 用来解决两个接口不兼容问题，由一个对象来包装不兼容的对象，比如参数转换，允许直接访问

```javascript
class Adapter {
    money () {
        return '人民币'
    }
}

class AdapterWrapper {
    constructor () {
        this.Adapter = new Adapter()
    }

    m2$ () {
        const m = this.Adapter.money()
        return `人民币兑换成美元`
    }
}

const adapterWrapper = new AdapterWrapper()
adapterWrapper.m2$()
```

应用场景：多个对象合并成一个对象

4. 装饰器模式（AOP编程）

> 在不改变源对象的自身方法的基础上，给源对象自身方法提供新的功能

```javascript
class Source {
    add (a, b) {
        return a + b
    }
}

class DecorateSource {
    constructor () {
        this.source = new Source()
    }
    add (a, b) {
        console.log('传入的参数为', a, b)
        return this.source.add(a, b)
    }
}

const decorateSource = new DecorateSource()
decorateSource.add(1, 2) // 传入的参数为 1 2     3
```

应用场景：

- 处理ajax异常上报，数据分析
- Vue中处理数组变异方法

5. 观察者模式

> 定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都将得到通知

```javascript
class Sub {
    constructor () {
        this.observers = []
    }
    attach (observer) {
        this.observers.push(observer)
    }
    notify () {
        this.observers.forEach(observer => {
            observer.update()
        } )
    }
}

class Observer {
    constructor (name) {
        this.name = name
    }
    update () {
        console.log(`${this.name}触发更新`)
    }
}

const observerA = new Observer('A')
const observerB = new Observer('B')
const sub = new Sub()
sub.attach(observerA)
sub.attach(observerB)
sub.notify()

```

应用场景：JS事件、promise、Vue的watch方法

与订阅/发布模式区别 主要在于调度不同。观察者模式由具体目标方法调度，而订阅发布模式由统一调度中心去调度，所以观察者模式的观察者和目标会有依赖，而后者没有。
