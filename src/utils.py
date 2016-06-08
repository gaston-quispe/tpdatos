# particiona el vector 'vec_in' en dos vectores
# porcentaje_train: 0 a 1 . Porcentaje de muestras
# que se van a vec_out_train
def particionar_train_test(vec_in, porcentaje_train):
    vec_out_train = vec_in[:porcentaje_train*len(vec_in),:]
    vec_out_test  = vec_in[porcentaje_train*len(vec_in):,:]

    return vec_out_train, vec_out_test