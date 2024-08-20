# Import the necessary libraries
import os, argparse


# Function that parces the different variables
def variables_parcing():
    """
    Parse the different variables that are passed as arguments to the script.        

    Parameters
    ----------
    none.
        
    Returns
    -------
    argparse.Namespace
        The different variables that are passed as arguments to the script.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_epochs', type=int, default=50)        
    parser.add_argument('--checkpoint_dir', type=str, default='checkpoint')        
    parser.add_argument('--log_dir', type=str, default='logs')
    parser.add_argument('--data_dir', type=str, default='data')
    parser.add_argument('--dataset', type=str, default='assistments_2009_2010_skillBuilder.csv')
    parser.add_argument('--anneal_interval', type=int, default=20)
    parser.add_argument('--maxgradnorm', type=float, default=50.0)
    parser.add_argument('--momentum', type=float, default=0.9)
    parser.add_argument('--initial_lr', type=float, default=0.05)
    parser.add_argument('--lr_decay', type=float, default=0.92)
    parser.add_argument('--keep_prob', type=float, default=0.6)
    parser.add_argument('--hidden_layer', type=int, default=200)
    parser.add_argument('--input_layer', type=int, default=200)
    parser.add_argument('--num_layers', type=int, default=1)
    parser.add_argument('--model', type=str, default='DKT')
    parser.add_argument('--n_questions', type=int, default=110)
    parser.add_argument('--seq_len', type=int, default=200)
    parser.add_argument('--batch_size', type=int, default=32)	
    parser.add_argument('--test_size', type=float, default=0.2)
    parser.add_argument('--train_size', type=float, default=0.8)
    parser.add_argument('--seed', type=int, default=0)
    args = parser.parse_args()
    
    print(args)
    # if not os.path.exists(args.checkpoint_dir):
	# 	os.mkdir(args.checkpoint_dir)
	# if not os.path.exists(args.log_dir):
	# 	os.mkdir(args.log_dir)
	# if not os.path.exists(args.data_dir):
	# 	os.mkdir(args.data_dir)
	# raise Exception('Need data set')

    return args

    
