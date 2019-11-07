(function() {

// Chart design based on the recommendations of Stephen Few. Implementation
// based on the work of Clint Ivy, Jamie Love, and Jason Davies.
// http://projects.instantcognition.com/protovis/bulletchart/

// 子弹图是由Stephen Few设计发明的，Stephen Few现在是数据可视化方向的领先专家。
d3.bullet = function() {
  var orient = "left", // 定义子弹图默认的方向，为横向自左向右
      reverse = false, // 定义子弹图默认的方向是否与orient相反，如果为true,则子弹图横向自右向
                       // 左，即度量刻度方向反转
      duration = 0,
      ranges = bulletRanges,     // 定义子弹图默认定性范围获取方法为bulletRanges()
      markers = bulletMarkers,   // 定义子弹图默认主要标记标识获取方法为bulletMarkers()
      measures = bulletMeasures, // 定义子弹图默认刻度量表获取方法为bulletMeasures()
      width = 380,               // 定义默认宽度
      height = 30,               // 定义默认高度
      tickFormat = null;         // 定义默认坐标刻度格式

  // For each small multiple…
  // 生成子弹图的核心方法
  function bullet(g) {
    // 这里的参数g，是添加的group元素数组
    // 这里的参数d是g元素所绑定的data，i是循环index值
    g.each(function(d, i) {
      // 获取d中的ranges数组的值，并且对其进行降序排序,这里的this指向g
      var rangez = ranges.call(this, d, i).slice().sort(d3.descending),
          // 获取d中的markers数组的值，并且对其进行降序排序,这里的this指向g
          markerz = markers.call(this, d, i).slice().sort(d3.descending),
          // 获取d中的measures数组的值，并且对其进行降序排序,这里的this指向g
          measurez = measures.call(this, d, i).slice().sort(d3.descending),
          // 用已经获得了ranges,markers和measures的this来更新g
          g = d3.select(this);

      // Compute the new x-scale.
      // 定义坐标轴为线性坐标，定义定义域，值域，值域这里根据reverse属性来确定方向
      var x1 = d3.scale.linear()
          .domain([0, Math.max(rangez[0], markerz[0], measurez[0])])
          .range(reverse ? [width, 0] : [0, width]);

      // Retrieve the old x-scale, if this is an update.
      var x0 = this.__chart__ || d3.scale.linear()
          .domain([0, Infinity])
          .range(x1.range());

      // Stash the new scale.
      this.__chart__ = x1;

      // Derive width-scales from the x-scales.
      // 计算子弹图定性范围的宽度
      var w0 = bulletWidth(x0),
          w1 = bulletWidth(x1);

      // Update the range rects.
      // 为定性范围矩形条绑定定性范围数据
      var range = g.selectAll("rect.range")
          .data(rangez);
      // 生成定性范围矩形条，并且定义class属性，以便控制不同定性范围的颜色
      range.enter().append("rect")
          .attr("class", function(d, i) { return "range s" + i; })
          .attr("width", w0) // 定义定性范围矩形条的宽度
          .attr("height", height)
          .attr("x", reverse ? x0 : 0)
        .transition()
          .duration(duration)
          .attr("width", w1)
          .attr("x", reverse ? x1 : 0);
      // 启动转变函数transition()在duration时间间隔内绘制定性范围矩形
      range.transition()
          .duration(duration)
          .attr("x", reverse ? x1 : 0)
          .attr("width", w1)
          .attr("height", height);

      // Update the measure rects.
      // 为刻度量表绑定数据
      var measure = g.selectAll("rect.measure")
          .data(measurez);
      // 生成刻度量表，即主体数据条柱，并且定义class属性，以便控制不同主体数据的颜色
      measure.enter().append("rect")
          .attr("class", function(d, i) { return "measure s" + i; })
          .attr("width", w0)
          .attr("height", height / 3)
          .attr("x", reverse ? x0 : 0)
          .attr("y", height / 3)
        .transition()
          .duration(duration)
          .attr("width", w1)
          .attr("x", reverse ? x1 : 0);
      // 启动转变函数transition()在duration时间间隔内绘制主体数据条柱
      measure.transition()
          .duration(duration)
          .attr("width", w1)
          .attr("height", height / 3)
          .attr("x", reverse ? x1 : 0)
          .attr("y", height / 3);

      // Update the marker lines.
      // 为子弹图的标记标识绑定数据
      var marker = g.selectAll("line.marker")
          .data(markerz);
      // 生成标记标识线，
      marker.enter().append("line")
          .attr("class", "marker")
          .attr("x1", x0)
          .attr("x2", x0)
          .attr("y1", height / 6)
          .attr("y2", height * 5 / 6)
        .transition()
          .duration(duration)
          .attr("x1", x1)
          .attr("x2", x1);
      // 启动转变函数transition()在duration时间间隔内绘制标记标识线
      marker.transition()
          .duration(duration)
          .attr("x1", x1)
          .attr("x2", x1)
          .attr("y1", height / 6)
          .attr("y2", height * 5 / 6);

      // Compute the tick format.
      // 计算坐标刻度的格式
      var format = tickFormat || x1.tickFormat(8);

      // Update the tick groups.
      // 为坐标刻度绑定数据
      var tick = g.selectAll("g.tick")
          .data(x1.ticks(8), function(d) {
            return this.textContent || format(d);
          });

      // Initialize the ticks with the old scale, x0.
      // 初始化刻度
      var tickEnter = tick.enter().append("g")
          .attr("class", "tick")
          .attr("transform", bulletTranslate(x0))
          .style("opacity", 1e-6);
      // 定义刻度线
      tickEnter.append("line")
          .attr("y1", height)
          .attr("y2", height * 7 / 6);
      // 定义刻度文本
      tickEnter.append("text")
          .attr("text-anchor", "middle")
          .attr("dy", "1em")
          .attr("y", height * 7 / 6)
          .text(format);

      // Transition the entering ticks to the new scale, x1.
      tickEnter.transition()
          .duration(duration)
          .attr("transform", bulletTranslate(x1))
          .style("opacity", 1);

      // Transition the updating ticks to the new scale, x1.
      var tickUpdate = tick.transition()
          .duration(duration)
          .attr("transform", bulletTranslate(x1))
          .style("opacity", 1);

      tickUpdate.select("line")
          .attr("y1", height)
          .attr("y2", height * 7 / 6);

      tickUpdate.select("text")
          .attr("y", height * 7 / 6);

      // Transition the exiting ticks to the new scale, x1.
      tick.exit().transition()
          .duration(duration)
          .attr("transform", bulletTranslate(x1))
          .style("opacity", 1e-6)
          .remove();
    });
    d3.timer.flush();
  }

  // left, right, top, bottom
  //定义子弹图方向和是否反转的计算方法
  bullet.orient = function(x) {
    if (!arguments.length) return orient;
    orient = x;
    // 子弹图的reverse属性的计算规则为，如果orient为从右向左或者orient为自底向上，则反转坐标轴；否
    // 则，不进行反转
    reverse = orient == "right" || orient == "bottom";
    return bullet;
  };


  // ranges (bad, satisfactory, good)
  // 定义子弹图的定性范围方法，例如bad,satisfactroy,good三个等级
  bullet.ranges = function(x) {
    if (!arguments.length) return ranges;
    ranges = x;
    return bullet;
  };

  // markers (previous, goal)
  // 定义子弹图的重要标识关键点方法
  bullet.markers = function(x) {
    if (!arguments.length) return markers;
    markers = x;
    return bullet;
  };

  // measures (actual, forecast)
  // 定义子弹图的刻度量表方法
  bullet.measures = function(x) {
    if (!arguments.length) return measures;
    measures = x;
    return bullet;
  };

  //设置子弹图宽度的方法
  bullet.width = function(x) {
    if (!arguments.length) return width;
    width = x;
    return bullet;
  };
   //设置子弹图高度的方法
  bullet.height = function(x) {
    if (!arguments.length) return height;
    height = x;
    return bullet;
  };

  // 定义子弹图的坐标刻度格式方法
  bullet.tickFormat = function(x) {
    if (!arguments.length) return tickFormat;
    tickFormat = x;
    return bullet;
  };
  // 设置子弹图的duration属性值
  bullet.duration = function(x) {
    if (!arguments.length) return duration;
    duration = x;
    return bullet;
  };

  // 返回子弹图对象
  return bullet;
};
// 子弹图的定性范围获取方法
function bulletRanges(d) {
  return d.ranges;
}
// 子弹图的主要标识获取方法
function bulletMarkers(d) {
  return d.markers;
}
// 子弹图的刻度量表获取方法
function bulletMeasures(d) {
  return d.measures;
}
// 子弹图刻度的转换计算方法
function bulletTranslate(x) {
  return function(d) {
    return "translate(" + x(d) + ",0)";
  };
}
//由x坐标计算方式来得出子弹图宽度坐标的计算方式
function bulletWidth(x) {
  var x0 = x(0);
  return function(d) {
    return Math.abs(x(d) - x0);
  };
}

})();