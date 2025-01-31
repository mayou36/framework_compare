from gen import Gen
import tensorflow as tf

class GraphTensorFlow(Gen):

    def prepare(self):
        self.X_tf = tf.constant(self.X, dtype=tf.float32, name="X_tf")
        self.d_tf = tf.constant(self.d[:,None], dtype=tf.float32, name="d_tf")
        self.sess = tf.Session()
        
        f = 2 / self.N

        w = tf.Variable(tf.zeros((2, 1)), name="w_tf")
        self.w = w
        y = tf.matmul(self.X_tf, w, name="y_tf")
        e = y - self.d_tf
        grad = f * tf.matmul(tf.transpose(self.X_tf), e)

        self.training_op = tf.assign(w, w - self.mu * grad)
        init = tf.global_variables_initializer()
        self.sess.run(init)
        self.sess.run(self.training_op)


    def run(self):
        for epoch in range(self.N_epochs):
            self.sess.run(self.training_op)
        opt = self.sess.run(self.w)
        self.sess.close()
        return opt.squeeze()


if __name__ == '__main__':
    gen = GraphTensorFlow()
    gen.simple_time()
