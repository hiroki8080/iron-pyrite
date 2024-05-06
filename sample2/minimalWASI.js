class MinimalWASI {

  instance;

  constructor(){
    this.bind();
  }

  setInstance(instance){
    this.instance = instance;
  }

  start(){
    this.instance.exports._start();
  }

  args_get(){
    console.log('args_get');
    return 0;
  }

  args_sizes_get() {
    console.log('args_sizes_get');
    return 0;
  }

  environ_get() {
    console.log('environ_get');
    return 0;
  }

  environ_sizes_get() {
    console.log('environ_sizes_get');
    return 0;
  }

  clock_res_get() {
    console.log('clock_res_get');
    return 0;
  }

  clock_time_get() {
    console.log('clock_time_get');
    return 0;
  }

  fd_advise() {
    console.log('fd_advise');
    return 0;
  }

  fd_close() {
    console.log('fd_close');
    return 0;
  }

  fd_datasync() {
    console.log('fd_datasync');
    return 0;
  }

  fd_fdstat_get() {
    console.log('fd_fdstat_get');
    return 0;
  }

  fd_fdstat_set_flags() {
    console.log('fd_fdstat_set_flags');
    return 0;
  }

  fd_filestat_get() {
    console.log('fd_filestat_get');
    return 0;
  }

  fd_filestat_set_size() {
    console.log('fd_filestat_set_size');
    return 0;
  }

  fd_filestat_set_times() {
    console.log('fd_filestat_set_times');
    return 0;
  }

  fd_pread() {
    console.log('fd_pread');
    return 0;
  }

  fd_prestat_get() {
    console.log('fd_prestat_get');
    return 8;
  }

  fd_prestat_dir_name() {
    console.log('fd_prestat_dir_name');
    return 28;
  }

  fd_pwrite() {
    console.log('fd_pwrite');
    return 0;
  }

  fd_read(fd, iovsPtr, iovsLength, bytesReadPtr) {
    console.log('fd_read');
    return 0;
  }

  fd_readdir() {
    console.log('fd_readdir');
    return 0;
  }

  fd_seek() {
    console.log('fd_seek');
    return 0;
  }

  fd_sync() {
    console.log('fd_sync');
    return 0;
  }

  fd_tell(arg0, arg1) {
    console.log("fd_tell, arg0:" + arg0 + "arg1:" + arg1);
    return 0;
  }

  fd_write(fd, start, len, writePos) {
    const dataView = new DataView(this.instance.exports.memory.buffer);
    const textBuff = new Uint32Array(this.instance.exports.memory.buffer, start, len * 2);
    const decoder = new TextDecoder();
    if(fd === 1) {
      let text = "";
      let total = 0;
      for(let i =0; i < len * 2; i += 2){
          const offset = textBuff[i];
          const length = textBuff[i+1];
          const textChunk = decoder.decode(new Int8Array(this.instance.exports.memory.buffer, offset, length));
          text += textChunk;
          total += length;
      }
      dataView.setInt32(writePos, total, true);
      console.log(text);
    }
    return 0;
  }

  path_create_directory() {
    console.log('path_create_directory');
    return 0;
  }

  path_filestat_get() {
    console.log('path_filestat_get');
    return 0;
  }

  path_filestat_set_times() {
    console.log('path_filestat_set_times');
    return 0;
  }

  path_link() {
    console.log('path_link');
    return 0;
  }

  path_open() {
    console.log('path_open');
    return 0;
  }

  path_readlink() {
    console.log('path_readlink');
    return 0;
  }

  path_remove_directory() {
    console.log('path_remove_directory');
    return 0;
  }

  path_rename() {
    console.log('path_rename');
    return 0;
  }

  path_symlink() {
    console.log('path_symlink');
    return 0;
  }

  path_unlink_file() {
    console.log('path_unlink_file');
    return 0;
  }

  poll_oneoff() {
    console.log('poll_oneoff');
    return 0;
  }

  proc_exit() {
    console.log('proc_exit');
    return 0;
  }

  sched_yield() {
    console.log('sched_yield');
    return 0;
  }

  random_get() {
    console.log('random_get');
    return 0;
  }

  sock_accept() {
    console.log('sock_accept');
    return 0;
  }

  sock_recv() {
    console.log('sock_recv');
    return 0;
  }

  sock_send() {
    console.log('sock_send');
    return 0;
  }

  sock_shutdown() {
    console.log('sock_shutdown');
    return 0;
  }

  bind(){
    this.args_get = this.args_get.bind(this);
    this.args_sizes_get = this.args_sizes_get.bind(this);
    this.environ_get = this.environ_get.bind(this);
    this.environ_sizes_get = this.environ_sizes_get.bind(this);
    this.clock_res_get = this.clock_res_get.bind(this);
    this.clock_time_get = this.clock_time_get.bind(this);
    this.fd_advise = this.fd_advise.bind(this);
    this.fd_close = this.fd_close.bind(this);
    this.fd_datasync = this.fd_datasync.bind(this);
    this.fd_fdstat_get = this.fd_fdstat_get.bind(this);
    this.fd_fdstat_set_flags = this.fd_fdstat_set_flags.bind(this);
    this.fd_filestat_get = this.fd_filestat_get.bind(this);
    this.fd_filestat_set_size = this.fd_filestat_set_size.bind(this);
    this.fd_filestat_set_times = this.fd_filestat_set_times.bind(this);
    this.fd_pread = this.fd_pread.bind(this);
    this.fd_prestat_get = this.fd_prestat_get.bind(this);
    this.fd_prestat_dir_name = this.fd_prestat_dir_name.bind(this);
    this.fd_pwrite = this.fd_pwrite.bind(this);
    this.fd_read = this.fd_read.bind(this);
    this.fd_readdir = this.fd_readdir.bind(this);
    this.fd_seek = this.fd_seek.bind(this);
    this.fd_sync = this.fd_sync.bind(this);
    this.fd_tell = this.fd_tell.bind(this);
    this.fd_write = this.fd_write.bind(this);
    this.path_create_directory = this.path_create_directory.bind(this);
    this.path_filestat_get = this.path_filestat_get.bind(this);
    this.path_filestat_set_times = this.path_filestat_set_times.bind(this);
    this.path_link = this.path_link.bind(this);
    this.path_open = this.path_open.bind(this);
    this.path_readlink = this.path_readlink.bind(this);
    this.path_remove_directory = this.path_remove_directory.bind(this);
    this.path_rename = this.path_rename.bind(this);
    this.path_symlink = this.path_symlink.bind(this);
    this.path_unlink_file = this.path_unlink_file.bind(this);
    this.poll_oneoff = this.poll_oneoff.bind(this);
    this.proc_exit = this.proc_exit.bind(this);
    this.sched_yield = this.sched_yield.bind(this);
    this.random_get = this.random_get.bind(this);
    this.sock_accept = this.sock_accept.bind(this);
    this.sock_recv = this.sock_recv.bind(this);
    this.sock_send = this.sock_send.bind(this);
    this.sock_shutdown = this.sock_shutdown.bind(this);
  }

}