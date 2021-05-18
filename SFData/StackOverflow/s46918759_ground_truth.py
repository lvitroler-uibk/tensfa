import tensorflow as tf
V = 100
embeddings = tf.Variable(tf.random_normal([V, 1]))

norm_embed = tf.sqrt(tf.reduce_sum(tf.multiply(embeddings, embeddings), 1))
norm_embed = tf.reshape(norm_embed, [V, 1])
comparison = tf.greater(norm_embed, tf.constant(1.))
comparison = tf.reshape(comparison, [V])
cond_assignment = tf.assign(embeddings, tf.where(comparison, embeddings/norm_embed, embeddings))