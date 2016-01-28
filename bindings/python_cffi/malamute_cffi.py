################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Please refer to the README for information about making permanent changes.  #
################################################################################

from __future__ import print_function
import os
import re
import sys

from pyczmq._cffi import ffi

try:
    # If LD_LIBRARY_PATH or your OSs equivalent is set, this is the only way to
    # load the library.  If we use find_library below, we get the wrong result.
    if os.name == 'posix':
        if sys.platform == 'darwin':
            libpath = 'libmlm.0.dylib'
        else:
            libpath = 'libmlm.so.0'
    elif os.name == 'nt':
        libpath = 'libmlm.dll'
    lib = ffi.dlopen(libpath)
except OSError:
    libpath = find_library("malamute")
    if not libpath:
        raise ImportError("Unable to find libmlm")
    lib = ffi.dlopen(libpath)

# Custom setup for malamute
ffi.cdef('''
typedef struct _zactor_t zactor_t;
typedef struct _zsock_t zsock_t;
typedef struct _zmsg_t zmsg_t;
''')


cdefs = '''
typedef struct _mlm_proto_t mlm_proto_t;
typedef struct _zsock_t zsock_t;
typedef struct _zframe_t zframe_t;
typedef struct _zmsg_t zmsg_t;
typedef struct _mlm_client_t mlm_client_t;
typedef struct _zactor_t zactor_t;
// CLASS: mlm_proto
// Create a new empty mlm_proto
MLM_EXPORT mlm_proto_t *
    mlm_proto_new (void);

// Destroy a mlm_proto instance
MLM_EXPORT void
    mlm_proto_destroy (mlm_proto_t **self_p);

// Receive a mlm_proto from the socket. Returns 0 if OK, -1 if
// there was an error. Blocks if there is no message waiting. 
MLM_EXPORT int
    mlm_proto_recv (mlm_proto_t *self, zsock_t *input);

// Send the mlm_proto to the output socket, does not destroy it
MLM_EXPORT int
    mlm_proto_send (mlm_proto_t *self, zsock_t *output);

// Print contents of message to stdout
MLM_EXPORT void
    mlm_proto_print (mlm_proto_t *self);

// Get the message routing id, as a frame
MLM_EXPORT zframe_t *
    mlm_proto_routing_id (mlm_proto_t *self);

// Set the message routing id from a frame
MLM_EXPORT void
    mlm_proto_set_routing_id (mlm_proto_t *self, zframe_t *routing_id);

// Get the mlm_proto message id
MLM_EXPORT int
    mlm_proto_id (mlm_proto_t *self);

// Set the mlm_proto message id
MLM_EXPORT void
    mlm_proto_set_id (mlm_proto_t *self, int id);

// Get the mlm_proto message id as printable text
MLM_EXPORT const char *
    mlm_proto_command (mlm_proto_t *self);

// Get the address field
MLM_EXPORT const char *
    mlm_proto_address (mlm_proto_t *self);

// Set the address field
MLM_EXPORT void
    mlm_proto_set_address (mlm_proto_t *self, const char *address);

// Get the stream field
MLM_EXPORT const char *
    mlm_proto_stream (mlm_proto_t *self);

// Set the stream field
MLM_EXPORT void
    mlm_proto_set_stream (mlm_proto_t *self, const char *stream);

// Get the pattern field
MLM_EXPORT const char *
    mlm_proto_pattern (mlm_proto_t *self);

// Set the pattern field
MLM_EXPORT void
    mlm_proto_set_pattern (mlm_proto_t *self, const char *pattern);

// Get the subject field
MLM_EXPORT const char *
    mlm_proto_subject (mlm_proto_t *self);

// Set the subject field
MLM_EXPORT void
    mlm_proto_set_subject (mlm_proto_t *self, const char *subject);

// Get a copy of the content field
MLM_EXPORT zmsg_t *
    mlm_proto_content (mlm_proto_t *self);

// Get the content field and transfer ownership to caller
MLM_EXPORT zmsg_t *
    mlm_proto_get_content (mlm_proto_t *self);

// 
MLM_EXPORT void
    mlm_proto_set_content (mlm_proto_t *self, zmsg_t **content_p);

// Get the sender field
MLM_EXPORT const char *
    mlm_proto_sender (mlm_proto_t *self);

// Set the sender field
MLM_EXPORT void
    mlm_proto_set_sender (mlm_proto_t *self, const char *sender);

// Get the tracker field
MLM_EXPORT const char *
    mlm_proto_tracker (mlm_proto_t *self);

// Set the tracker field
MLM_EXPORT void
    mlm_proto_set_tracker (mlm_proto_t *self, const char *tracker);

// Get the timeout field
MLM_EXPORT uint32_t
    mlm_proto_timeout (mlm_proto_t *self);

// Set the timeout field
MLM_EXPORT void
    mlm_proto_set_timeout (mlm_proto_t *self, uint32_t timeout);

// Get the status_code field
MLM_EXPORT uint16_t
    mlm_proto_status_code (mlm_proto_t *self);

// Set the status_code field
MLM_EXPORT void
    mlm_proto_set_status_code (mlm_proto_t *self, uint16_t status_code);

// Get the status_reason field
MLM_EXPORT const char *
    mlm_proto_status_reason (mlm_proto_t *self);

// Set the status_reason field
MLM_EXPORT void
    mlm_proto_set_status_reason (mlm_proto_t *self, const char *status_reason);

// Get the amount field
MLM_EXPORT uint16_t
    mlm_proto_amount (mlm_proto_t *self);

// Set the amount field
MLM_EXPORT void
    mlm_proto_set_amount (mlm_proto_t *self, uint16_t amount);

// Self test of this class.
MLM_EXPORT void
    mlm_proto_test (bool verbose);

// CLASS: mlm_server
// Self test of this class.
MLM_EXPORT void
    mlm_server_test (bool verbose);

// CLASS: mlm_client
// Create a new mlm_client, return the reference if successful, or NULL
// if construction failed due to lack of available memory.             
MLM_EXPORT mlm_client_t *
    mlm_client_new (void);

// Destroy the mlm_client and free all memory used by the object.
MLM_EXPORT void
    mlm_client_destroy (mlm_client_t **self_p);

// Return actor, when caller wants to work with multiple actors and/or
// input sockets asynchronously.                                      
MLM_EXPORT zactor_t *
    mlm_client_actor (mlm_client_t *self);

// Return message pipe for asynchronous message I/O. In the high-volume case,
// we send methods and get replies to the actor, in a synchronous manner, and
// we send/recv high volume message data to a second pipe, the msgpipe. In   
// the low-volume case we can do everything over the actor pipe, if traffic  
// is never ambiguous.                                                       
MLM_EXPORT zsock_t *
    mlm_client_msgpipe (mlm_client_t *self);

// Return true if client is currently connected, else false. Note that the   
// client will automatically re-connect if the server dies and restarts after
// a successful first connection.                                            
MLM_EXPORT bool
    mlm_client_connected (mlm_client_t *self);

// Set PLAIN authentication username and password. If you do not call this, the
// client will use NULL authentication. TODO: add "set curve auth".            
// Returns >= 0 if successful, -1 if interrupted.                              
MLM_EXPORT int
    mlm_client_set_plain_auth (mlm_client_t *self, const char *username, const char *password);

// Connect to server endpoint, with specified timeout in msecs (zero means wait
// forever). Constructor succeeds if connection is successful. The caller may  
// specify its address.                                                        
// Returns >= 0 if successful, -1 if interrupted.                              
MLM_EXPORT int
    mlm_client_connect (mlm_client_t *self, const char *endpoint, uint32_t timeout, const char *address);

// Prepare to publish to a specified stream. After this, all messages are sent to
// this stream exclusively.                                                      
// Returns >= 0 if successful, -1 if interrupted.                                
MLM_EXPORT int
    mlm_client_set_producer (mlm_client_t *self, const char *stream);

// Consume messages with matching subjects. The pattern is a regular expression    
// using the CZMQ zrex syntax. The most useful elements are: ^ and $ to match the  
// start and end, . to match any character, \s and \S to match whitespace and      
// non-whitespace, \d and \D to match a digit and non-digit, \a and \A to match    
// alphabetic and non-alphabetic, \w and \W to match alphanumeric and              
// non-alphanumeric, + for one or more repetitions, * for zero or more repetitions,
// and ( ) to create groups. Returns 0 if subscription was successful, else -1.    
// Returns >= 0 if successful, -1 if interrupted.                                  
MLM_EXPORT int
    mlm_client_set_consumer (mlm_client_t *self, const char *stream, const char *pattern);

// Offer a particular named service, where the pattern matches request subjects
// using the CZMQ zrex syntax.                                                 
// Returns >= 0 if successful, -1 if interrupted.                              
MLM_EXPORT int
    mlm_client_set_worker (mlm_client_t *self, const char *address, const char *pattern);

// Send STREAM SEND message to server, takes ownership of message
// and destroys message when done sending it.                    
MLM_EXPORT int
    mlm_client_send (mlm_client_t *self, const char *subject, zmsg_t **content_p);

// Send MAILBOX SEND message to server, takes ownership of message
// and destroys message when done sending it.                     
MLM_EXPORT int
    mlm_client_sendto (mlm_client_t *self, const char *address, const char *subject, const char *tracker, uint32_t timeout, zmsg_t **content_p);

// Send SERVICE SEND message to server, takes ownership of message
// and destroys message when done sending it.                     
MLM_EXPORT int
    mlm_client_sendfor (mlm_client_t *self, const char *address, const char *subject, const char *tracker, uint32_t timeout, zmsg_t **content_p);

// Receive message from server; caller destroys message when done
MLM_EXPORT zmsg_t *
    mlm_client_recv (mlm_client_t *self);

// Return last received command. Can be one of these values:
//     "STREAM DELIVER"                                     
//     "MAILBOX DELIVER"                                    
//     "SERVICE DELIVER"                                    
MLM_EXPORT const char *
    mlm_client_command (mlm_client_t *self);

// Return last received status
MLM_EXPORT int
    mlm_client_status (mlm_client_t *self);

// Return last received reason
MLM_EXPORT const char *
    mlm_client_reason (mlm_client_t *self);

// Return last received address
MLM_EXPORT const char *
    mlm_client_address (mlm_client_t *self);

// Return last received sender
MLM_EXPORT const char *
    mlm_client_sender (mlm_client_t *self);

// Return last received subject
MLM_EXPORT const char *
    mlm_client_subject (mlm_client_t *self);

// Return last received content
MLM_EXPORT zmsg_t *
    mlm_client_content (mlm_client_t *self);

// Return last received tracker
MLM_EXPORT const char *
    mlm_client_tracker (mlm_client_t *self);

// Send multipart string message to stream, end list with NULL        
// Returns 0 if OK, -1 if failed due to lack of memory or other error.
MLM_EXPORT int
    mlm_client_sendx (mlm_client_t *self, const char *subject, const char *content, ...);

// Send multipart string to mailbox, end list with NULL               
// Returns 0 if OK, -1 if failed due to lack of memory or other error.
MLM_EXPORT int
    mlm_client_sendtox (mlm_client_t *self, const char *address, const char *subject, const char *content, ...);

// Send multipart string to service, end list with NULL               
// Returns 0 if OK, -1 if failed due to lack of memory or other error.
MLM_EXPORT int
    mlm_client_sendforx (mlm_client_t *self, const char *address, const char *subject, const char *content, ...);

// Receive a subject and string content from the server. The content may be
// 1 or more string frames. This method is orthogonal to the sendx methods.
// End the string arguments with NULL. If there are not enough frames in   
// the received message, remaining strings are set to NULL. Returns number 
// of string contents received, or -1 in case of error. Free the returned  
// subject and content strings when finished with them. To get the type of 
// the command, use mlm_client_command ().                                 
MLM_EXPORT int
    mlm_client_recvx (mlm_client_t *self, char **subject_p, char **string_p, ...);

// Self test of this class.
MLM_EXPORT void
    mlm_client_test (bool verbose);

// CLASS: mlm_msg
// Self test of this class.
MLM_EXPORT void
    mlm_msg_test (bool verbose);

// CLASS: mlm_stream_simple
// Self test of this class.
MLM_EXPORT void
    mlm_stream_simple_test (bool verbose);

// CLASS: mlm_mailbox_simple
// Self test of this class.
MLM_EXPORT void
    mlm_mailbox_simple_test (bool verbose);

'''
cdefs = cdefs.replace('MLM_EXPORT', '')
cdefs = re.sub(r'CHECK_PRINTF\s*\([^)]\)\s*', '', cdefs)
cdefs = re.sub(r';[^;]*\bva_list\b[^;]*;', ';', cdefs, flags=re.S) # we don't support anything with a va_list arg

ffi.cdef(cdefs)