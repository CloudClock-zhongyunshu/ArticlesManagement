document.querySelector('.img__btn').addEventListener('click', function() {
    document.querySelector('.content').classList.toggle('s--signup')
})

    //导入操作
      //首先监听input框的变动，选中一个新的文件会触发change事件
      document.querySelector('#file').addEventListener('change', () => {
        //获取到选中的文件
        var file = document.querySelector('#file').files[0];
        let title = document.querySelector('.title');
        let title_name = document.createElement('span');
        title_name.innerHTML = `${file.name}`;
        title.append(title_name);
        var type = file.name.split('.');
        if (
          type[type.length - 1] !== 'xlsx' &&
          type[type.length - 1] !== 'xls'
        ) {
          alert('只能选择excel文件导入');
          return false;
        }
        const reader = new FileReader();
        reader.readAsBinaryString(file);
        reader.onload = (e) => {
          const data = e.target.result;
          const zzexcel = window.XLS.read(data, {
            type: 'binary',
          });
          const result = [];
          for (let i = 0; i < zzexcel.SheetNames.length; i++) {
            const newData = window.XLS.utils.sheet_to_json(
              zzexcel.Sheets[zzexcel.SheetNames[i]]
            );
            result.push(...newData);
          }
          const result_title = [];
          for (let key in result[0]) {
            result_title.push(key);
          }
          let table = document.querySelector('.table');
          let title_tr = document.createElement('tr');
          // 表头处理
          result_title.forEach((item, index) => {
            let title_th = document.createElement('th');
            title_th.innerHTML = `${item}`;
            title_tr.appendChild(title_th);
          });
          table.append(title_tr);
          // 内容处理
          result.forEach((item, index) => {
            let content_tr = document.createElement('tr');
            for (let key in item) {
              let content_td = document.createElement('td');
              content_td.innerHTML = `${item[key]}`;
              content_tr.appendChild(content_td);
            }
            table.append(content_tr);
          });
        };
      });


