
import tensorflow as tf
a= tf.constant(6,name='a_cons')
b=tf.constant(3,name='b_cons')
div=tf.div(a,b,name='div')
sess=tf.Session()
sess.run(div)
